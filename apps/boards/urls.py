from django.urls import path

from . import views

urlpatterns = [
    path('', views.BoardView.as_view()),
    path('<int:pk>', views.BoardDetailView.as_view()),
]
