from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Run
from .forms import CommentForm

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

    queryset = Run.objects.all()
    run = get_object_or_404(queryset, slug=slug)
    comments = run.comments.all().order_by("-created_on")
    comment_count = run.comments.filter(approved=True).count()

    if request.method == "POST":
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.run = run
        comment.save()
        messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted successfully!'
        )


    comment_form = CommentForm()

    return render(
        request,
        "runs/run_detail.html",
        {"run": run,
         "comments": comments,
         "comment_count": comment_count,
         "comment_form": comment_form,
         },
    )