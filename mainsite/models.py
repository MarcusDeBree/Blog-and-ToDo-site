from django.db import models


class Task(models.Model):
    name_task = models.CharField(max_length=255, verbose_name="New task")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name_task


class Blog(models.Model):
    article_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    main_text = models.TextField()
    date = models.DateField(auto_now=True)
    picture = models.ImageField(null=True, blank=True, upload_to="gallery", height_field=None, width_field=None,
                                max_length=100)

    def __str__(self):
        return self.article_name
