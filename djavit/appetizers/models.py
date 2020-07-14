from django.db import models
from django.urls import reverse


class Video(models.Model):
    title = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    vimeo_id = models.CharField(max_length=32)
    creation = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('appetizers:video', args=(self.slug,))

    def __str__(self):
        return f'Video: {self.title}'
