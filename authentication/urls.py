from django.urls import path
from .views import RegisterView
from . import views

urlpatterns = [
    path('register', RegisterView.as_view()),
    # path('', views.index),
]
