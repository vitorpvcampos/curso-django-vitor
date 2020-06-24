from django.urls import path

from djavit.appetizers.views import video

app_name = 'appetizers'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
]
