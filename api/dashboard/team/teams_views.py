# api/dashboard/teams/teams_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from db.teams import Teams
from utils.response import CustomResponse

from .teams_serializer import TeamsSerializer

class TeamsListCreateView(APIView):
    def get(self, request):
        teams = Teams.objects.all()
        serializer = TeamsSerializer(teams, many=True)
        return CustomResponse(response=serializer.data).get_success_response()

    def post(self, request):
        serializer = TeamsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(response=serializer.data).get_success_response()
        return CustomResponse(response=serializer.errors).get_failure_response()
