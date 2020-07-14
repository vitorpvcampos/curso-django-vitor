from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel


class Module(OrderedModel):
    title = models.CharField(max_length=64)
    public = models.TextField()
    description = models.TextField()
    slug = models.SlugField(unique=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('modules:detail', kwargs={'slug': self.slug})
