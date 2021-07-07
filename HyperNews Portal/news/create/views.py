from django.shortcuts import render
from django.views import View
from django.conf import settings
import json
from django.shortcuts import redirect
import random
from datetime import datetime
class CreateView(View):
    def get(self, request, *args, **kwargs):
       return render(request, "news/post.html")


    def post(self, request, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, 'r+') as f:
            title = request.POST.get('title')
            text = request.POST.get('text')
            news = json.load(f)
            new = {"created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "text": text, "title": title, "link": random.randint(4, 100)}
            news.append(new)
            f.seek(0)
            json.dump(news, f, indent=4)
        return redirect('/news')


