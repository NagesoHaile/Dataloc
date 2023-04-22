from django.urls import path

from .views import UserView

urlpatterns = [
    path('profile/<int:pk>/', UserView.as_view()),
]

