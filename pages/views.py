from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = 'about.html'
