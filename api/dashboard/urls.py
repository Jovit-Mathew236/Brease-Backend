from django.urls import path, include

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('project/', include('api.dashboard.project.urls')),
]
