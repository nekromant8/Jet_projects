from flask import Flask, abort, request
from flask_restful import Api, Resource, inputs, reqparse, fields, marshal_with
from datetime import date
import sys
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event.db'


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)


db.create_all()

parser = reqparse.RequestParser()
parser.add_argument(
    'event',
    type=str,
    help='The event name is required!',
    required=True
)
parser.add_argument(
    'date',
    type=inputs.date,
    help='The event date with the correct format is required! The correct format is YYYY-MM-DD!',
    required=True
)

parser.add_argument(
    'start_time',
    type=inputs.date,
    help='The event date with the correct format is required! The correct format is YYYY-MM-DD!',
    required=False
)
parser.add_argument(
    'end_time',
    type=inputs.date,
    help='The event date with the correct format is required! The correct format is YYYY-MM-DD!',
    required=False
)
resource_fields = {
    'id': fields.Integer,
    'event': fields.String,
    'date': fields.DateTime(dt_format='iso8601')
}


class EventByID(Resource):
    @marshal_with(resource_fields)
    def get(self, event_id):
        return event_id

    @marshal_with(resource_fields)
    def get(self, event_id):
        event = Event.query.filter(Event.id == event_id).first()
        if event is None:
            abort(404, "The event doesn't exist!")
        return event

    @staticmethod
    def delete(event_id):
        event = Event.query.filter(Event.id == event_id).first()
        if event is None:
            abort(404, "The event doesn't exist!")
        else:
            db.session.delete(event)
            db.session.commit()
            return {"message": "The event has been deleted!"}


class TodayEventsResource(Resource):
    @marshal_with(resource_fields)
    def get(self, **kwargs):
        events = Event.query.filter(Event.date == date.today()).all()
        return list(events)


class AddEventResource(Resource):
    @marshal_with(resource_fields)
    def get(self, **kwargs):
        start_time = request.args.get('start_time')
        end_time = request.args.get('end_time')
        if start_time or end_time:
            events = Event.query.filter(Event.date >= start_time, Event.date <= end_time).all()
        else:
            events = Event.query.all()
        return events

    @staticmethod
    def post():
        args = parser.parse_args()
        event = Event(event=args['event'], date=args['date'].date())
        db.session.add(event)
        db.session.commit()

        return {
            'message': 'The event has been added!',
            'event': args['event'],
            'date': str(args['date'].date())
        }


api.add_resource(EventByID, '/event/<int:event_id>')
api.add_resource(TodayEventsResource, '/event/today')
api.add_resource(AddEventResource, '/event')

# do not change the way you run the program
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
