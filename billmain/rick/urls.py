from django.urls import path

from . import views

app_name = 'rick'

urlpatterns = [
    path('', views.index, name='index'),
    path('rick/', views.profile, name='profile')
]
