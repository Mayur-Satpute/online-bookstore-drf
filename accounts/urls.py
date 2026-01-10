from django.urls import path
from .views import (
    SignupAPIView,
    LoginAPIView,
    LogoutAPIView,
    ForgotPasswordAPIView,
    ResetPasswordAPIView,
)

urlpatterns = [
    path("signup/", SignupAPIView.as_view()),
    path("login/", LoginAPIView.as_view()),
    path("logout/", LogoutAPIView.as_view()),
    path("forgot-password/", ForgotPasswordAPIView.as_view()),
    path("reset-password/<int:uid>/<str:token>/", ResetPasswordAPIView.as_view()),
]
