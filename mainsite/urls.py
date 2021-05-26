from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'mainsite'

urlpatterns = [
    path('', views.index, name="main"),
    path('blog/<int:pk>/', views.blog_detail, name="blog_detail"),
    path('blog/create_blog', views.create_blog, name="create_blog"),
    path('to_do', views.todo, name='to_do'),
    path('delete/', views.delete_task, name='delete_task'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
]
