from http.client import ResponseNotReady
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from db.task import Task
from utils.response import CustomResponse

from . import task_serializer

class TaskView(APIView):
    def get(self, request):
        task = Task.objects.all()
        serializer = task_serializer.TaskSerializer(task, many=True)
        return CustomResponse(response=serializer.data).get_success_response()

    def post(self, request):
        serializer = task_serializer.TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(response=serializer.data).get_success_response()
        return CustomResponse(response=serializer.errors).get_failure_response()
    
    def patch(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
            serializer = task_serializer.TaskSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return CustomResponse(response=serializer.data).get_success_response()
            return CustomResponse(response=serializer.errors).get_failure_response()
        except Exception as e:
            return CustomResponse(general_message=str(e)).get_failure_response()