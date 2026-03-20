from django.contrib import admin
from .models import Run, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('post', 'author', 'approved', 'created_on')
    search_fields = ['author', 'post']
    summernote_fields = ('body',)

# Register your models here.
admin.site.register(Run)