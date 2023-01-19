# apps/user/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserSignUpView, UserSignInView, UserWithdrawalView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path("sign-up/", UserSignUpView.as_view()),
    path("sign-in/", UserSignInView.as_view()),
    path("<int:pk>/withdraw/", UserWithdrawalView.as_view()),
]