from django.contrib.admin import ModelAdmin, register

from djavit.appetizers.models import Video


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('title', 'slug', 'creation', 'vimeo_id')
    ordering = ('creation',)
    prepopulated_fields = {'slug': ('title',)}
