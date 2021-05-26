from django.forms import ModelForm
from mainsite.models import Task, Blog
from django import forms


class TaskForm (ModelForm):
    class Meta:
        model = Task
        fields = ["name_task"]


class BlogForm (ModelForm):
    class Meta:
        model = Blog
        widgets = {
            "description": forms.Textarea()
        }
        fields = ["article_name", "description", "main_text", "picture"]