from django.shortcuts import render, loader
from django.views import View
from django.conf import settings
import json

class PageView(View):
    def get(self, request, *args, **kwargs):
        index = int(kwargs['link'])
        with open(settings.NEWS_JSON_PATH, 'r') as f:
            news = json.load(f)
            context = {"news": news, "index": index}
        return render(request, "news/index.html", context=context)
class MainView(View):
    def get(self, request, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, 'r') as f:
            news = json.load(f)
            q = request.GET.get('q')
            context = {"news": news, "q": q}
            return render(request, "news/main.html", context=context)




