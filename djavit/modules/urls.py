from django.urls import path

from djavit.modules import views

app_name = 'modules'
urlpatterns = [
    path('<slug:slug>', views.detail, name='detail'),
    path('classes/<slug:slug>', views.classs, name='classs'),
]
