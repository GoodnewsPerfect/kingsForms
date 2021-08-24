from django.urls import path
from . import views

app_name = 'kingsForms'

urlpatterns = [
    path('', views.home, name="home")
]