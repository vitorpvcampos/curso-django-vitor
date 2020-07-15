from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from djavit.modules.models import Module, Classs


@admin.register(Module)
class ModuleAdmin(OrderedModelAdmin):
    list_display = ('title', 'public', 'move_up_down_links')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Classs)
class ClasssAdmin(OrderedModelAdmin):
    list_display = ('title', 'module', 'order', 'move_up_down_links')
    list_filter = ('module',)
    ordering = ('module', 'order')
    prepopulated_fields = {'slug': ('title',)}
