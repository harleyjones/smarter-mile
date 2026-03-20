from django.shortcuts import render
from django.views import generic
from .models import Run

# Create your views here.
class RunList(generic.ListView):
    queryset = Run.objects.all()
    template_name = "runs/index.html"
    paginate_by = 6