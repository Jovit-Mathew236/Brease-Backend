from django.urls import path

from . import teams_views

urlpatterns = [

    path('', teams_views.UserDetailsAPI.as_view())
]
