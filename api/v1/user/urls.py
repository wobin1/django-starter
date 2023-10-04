from django.urls import path
from .views import User, SingleUser

urlpatterns = [
    path('users/', User.as_view()),
    path('users/<str:id>', SingleUser.as_view()),
]