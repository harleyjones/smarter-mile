from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Run(models.Model):
    title = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="run_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    distance = models.FloatField()
    duration = models.DurationField()