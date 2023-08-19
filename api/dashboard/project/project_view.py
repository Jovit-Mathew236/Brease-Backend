from http.client import ResponseNotReady
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.response import CustomResponse

from db.projects import Project
from . import project_serializer

class ProjectView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = project_serializer.ProjectSerializer(projects, many=True)
        return CustomResponse(response=serializer.data).get_success_response()

    def post(self, request):
        serializer = project_serializer.ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseNotReady(serializer.data)
        return response(serializer.errors)