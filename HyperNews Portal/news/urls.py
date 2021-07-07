from django.urls import path
from news.views import MovieView

urlpatterns = [
    path('', MovieView.as_view()),
]
