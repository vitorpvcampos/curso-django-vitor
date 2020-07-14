from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from djavit.modules.models import Module


@admin.register(Module)
class ModuleAdmin(OrderedModelAdmin):
    list_display = ('title', 'public', 'move_up_down_links')
    prepopulated_fields = {'slug': ('title',)}
