from django.urls import path

from djavit.teams import views

app_name = 'teams'
urlpatterns = [
    path('', views.index, name='index'),
]
