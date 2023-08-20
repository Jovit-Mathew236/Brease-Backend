from rest_framework.views import APIView

from db.user import User
from utils.response import CustomResponse
from . import user_serializer

class UserDetailsAPI(APIView):
    
    def get(self, request):
        users = User.objects.all()  # QuerySet of User objects

        if users is None:
            return CustomResponse(
                general_message="No user data available"
            ).get_failure_response()

        # Assuming you want to serialize all users
        serializer = user_serializer.UserSerializer(users, many=True)  # Pass the QuerySet and set `many=True`

        response_data = serializer.data
        return CustomResponse(response=response_data).get_success_response()

class UserCreateAPI(APIView):
    
        def post(self, request):
            serializer = user_serializer.UserDetailsEditSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return CustomResponse(
                    general_message=serializer.data
                ).get_success_response()
            return CustomResponse(
                general_message=serializer.errors
            ).get_failure_response()


class UserEditAPI(APIView):

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            serializer = user_serializer.UserDetailsEditSerializer(user).data
            return CustomResponse(response=serializer).get_success_response()
        except Exception as e:
            return CustomResponse(general_message=str(e)).get_failure_response()

    def delete(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            user.active = False
            user.save()
            return CustomResponse(
                general_message="User deleted successfully"
            ).get_success_response()

        except Exception as e:
            return CustomResponse(general_message=str(e)).get_failure_response()

    def patch(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            serializer = user_serializer.UserDetailsEditSerializer(
                user, data=request.data, partial=True, context={"admin": user}
            )
            if serializer.is_valid():
                serializer.save()

                return CustomResponse(
                    general_message=serializer.data
                ).get_success_response()
            return CustomResponse(
                general_message=serializer.errors
            ).get_failure_response()
        except Exception as e:
            return CustomResponse(general_message=str(e)).get_failure_response()
