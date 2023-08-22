from django.urls import include, path
from . import teams_views, project_team_link_views

urlpatterns = [
    path('create/', teams_views.TeamsListCreateView.as_view(), name='teams-list-create'),
    path('project-team-links/', project_team_link_views.ProjectTeamLinkListCreateView.as_view(), name='project-team-link-list-create'),
    path('task/', include('api.dashboard.team.task.urls'))
]
