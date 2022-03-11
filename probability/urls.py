from django.urls import path
from . import views

app_name = 'probability'
urlpatterns = [
    path('', views.index, name='index')
]