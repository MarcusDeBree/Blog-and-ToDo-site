from django.shortcuts import render, redirect, get_object_or_404

from .forms import TaskForm, BlogForm
from .models import Task, Blog


def index(request):
    articles = Blog.objects.all()
    return render(request, "mainsite/index.html", {"articles": articles})


def create_blog(request):
    if request.method == "POST":
        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            blog_form.save()
            return redirect("/")
    else:
        blog_form = BlogForm()

    return render(request, "mainsite/base.html", {"blog_form": blog_form})


def blog_detail(request, pk):
    blogs = get_object_or_404(Blog, pk=pk)
    return render(request, "mainsite/blog_detail.html", {"blogs": blogs})


def todo(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/to_do")
    else:
        form = TaskForm()

    return render(request, "mainsite/to_do.html", {"form": form, "tasks": tasks})


def delete_task(request):
    do = Task.objects.last()

    if request.method == "POST":
        do.delete()
        return redirect("/to_do")

    return render(request, "mainsite/to_do.html", {"do": do})


def about(request):
    return render(request, "mainsite/about.html")


def contacts(request):
    return render(request, "mainsite/contacts.html")
