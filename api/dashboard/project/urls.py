from django.urls import path, include
from . import project_view

urlpatterns = [
    path('', project_view.ProjectView.as_view()),
]