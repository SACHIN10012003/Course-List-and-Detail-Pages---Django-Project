from rest_framework import serializers
from .models import Course  # Assuming you have a Course model

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'  