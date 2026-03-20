from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Run(models.Model):
    title = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="run_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    distance = models.FloatField()
    hours = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    minutes = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(59)])
    seconds = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(59)])
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | By {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(
        Run, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.post.title} | By {self.author}"