from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
app_name = 'posts'


class PostTemplateView(TemplateView):
    template_name = 'posts/main.html'
