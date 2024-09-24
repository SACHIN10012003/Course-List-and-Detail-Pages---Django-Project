from django.urls import path
from .views import course_list, course_detail

urlpatterns = [
    path('courses/', course_list, name='course_list'),
    path('courses/<str:course_id>/', course_detail, name='course_detail'),
]
