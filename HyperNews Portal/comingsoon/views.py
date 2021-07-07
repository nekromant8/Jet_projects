from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
class SoonView(View):
    def get(self, request, *args, **kwargs):
        return redirect('/news')
