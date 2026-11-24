from django.urls import path

from academics.views import CourseListView
from academics.views import CourseCreateView
from academics.views import CourseRetrieveView
from academics.views import CourseUpdateDeleteView

urlpatterns=[
                path('course/list/',CourseListView.as_view()),
                path('course/add/',CourseCreateView.as_view()),
                path('course/get/<int:pk>/',CourseRetrieveView.as_view()),
                path('course/<int:pk>/',CourseUpdateDeleteView.as_view()),
]