from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from accounts.views import TrainerCreateView
from accounts.views import StudentCreateView
from accounts.views import TrainerProfileUpdateView
from accounts.views import StudentProfileUpdateView
from accounts.views import TrainerDetailView
from accounts.views import StudentDetailView

urlpatterns=[
                path('trainer/register/',TrainerCreateView.as_view()),
                path('student/register/',StudentCreateView.as_view()),

                path('trainer/profile/edit/',TrainerProfileUpdateView.as_view()),
                path('student/profile/edit/',StudentProfileUpdateView.as_view()),

                path('trainer/profile/',TrainerDetailView.as_view()),
                path('student/profile/',StudentDetailView.as_view()),

                path('token/',ObtainAuthToken.as_view()),
]