from django.contrib import admin

from djavit.teams.models import Team


class SubscriptionInline(admin.TabularInline):
    model = Team.students.through
    extra = 1
    readonly_fields = ('date',)
    autocomplete_fields = ('user',)
    ordering = ('-date',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = [SubscriptionInline]
    list_display = ('name', 'slug', 'start', 'end')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-start',)
