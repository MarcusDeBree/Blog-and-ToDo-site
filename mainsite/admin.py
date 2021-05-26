from django.contrib import admin
from mainsite.models import Task, Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('article_name', 'description', 'date')


admin.site.register(Task)
