from django.urls import path

from djavit.appetizers.views import video, index

app_name = 'appetizers'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
    path('', index, name='index'),
]
