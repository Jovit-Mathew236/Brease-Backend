from django.urls import path, include
from . import task_views

urlpatterns = [
    path('', task_views.TaskView.as_view()),
]