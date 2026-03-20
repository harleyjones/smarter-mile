from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Run, Comment
from .forms import CommentForm

# Create your views here.
class RunList(generic.ListView):
    queryset = Run.objects.filter(status=1)
    template_name = "blog/index.html"
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
    comments = run.comments.all().order_by("-created_on")
    comment_count = run.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = run
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "runs/run_detail.html",
        {
            "run": run,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Run.objects.filter(status=1)
        run = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = run
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('run_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Run.objects.filter(status=1)
    run = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('run_detail', args=[slug]))