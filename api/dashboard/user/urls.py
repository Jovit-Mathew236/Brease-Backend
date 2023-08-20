from django.urls import path

from . import user_views

urlpatterns = [

    path('details/', user_views.UserDetailsAPI.as_view()),
    path('create/', user_views.UserCreateAPI.as_view()),
    # path('', user_views.UserAPI.as_view(), name='list-user'),
    
    path('<str:user_id>/', user_views.UserEditAPI.as_view(), name="detail-user"),
    path('<str:user_id>/', user_views.UserEditAPI.as_view(), name="edit-user"),
    path('<str:user_id>/', user_views.UserEditAPI.as_view(), name="delete-user"),
]
