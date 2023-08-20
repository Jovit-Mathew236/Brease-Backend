from django.urls import path, include

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('project/', include('api.dashboard.project.urls')),
    # path('team/', include('api.dashboard.team.urls')),
    path('user/', include('api.dashboard.user.urls')),
    path('user/create', include('api.dashboard.user.urls')),
]
