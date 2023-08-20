from rest_framework.views import APIView
from rest_framework.response import Response
from db.projectteamlink import ProjectTeamLink
from utils.response import CustomResponse
from .project_team_link_serializer import ProjectTeamLinkSerializer

class ProjectTeamLinkListCreateView(APIView):
    def get(self, request):
        project_team_links = ProjectTeamLink.objects.all()
        serializer = ProjectTeamLinkSerializer(project_team_links, many=True)
        return CustomResponse(response=serializer.data).get_success_response()

    def post(self, request):
        serializer = ProjectTeamLinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(response=serializer.data).get_success_response()
        return CustomResponse(response=serializer.errors).get_failure_response()
