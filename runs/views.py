from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Run

# Create your views here.
class RunList(generic.ListView):
    queryset = Run.objects.all()
    template_name = "runs/index.html"
    paginate_by = 6

def run_detail(request, slug):
    """
    Display an individual :model:`runs.Run`.

    **Context**

    ``run``
        An instance of :model:`runs.Run`.

    **Template:**

    :template:`runs/run_detail.html`
    """

    queryset = Run.objects.filter(status=1)
    run = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "runs/run_detail.html",
        {"run": run},
    )