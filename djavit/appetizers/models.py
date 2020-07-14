from django.db import models
from django.urls import reverse


class Video(models.Model):
    slug = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    vimeo_id = models.CharField(max_length=32)

    def get_absolute_url(self):
        return reverse('appetizers:video', args=(self.slug,))
