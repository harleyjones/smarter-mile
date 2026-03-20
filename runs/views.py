from django.shortcuts import render
from django.views import generic
from .models import Run

# Create your views here.
class PostList(generic.ListView):
    queryset = Run.objects.all()
    template_name = "post_list.html"