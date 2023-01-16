from django.db.models import Avg
from rest_framework import serializers
from .models import Course, Assessment

class AssessmentSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Assessment
        fields = (
            'id',
            'id_course',
            'name',
            'email',
            'comment',
            'assessment',
            'create',
            'active'
        )

    def validate_assessment(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError('A avaliação Precisa ser um numero entre 1 a 5')


class CourseSerializer(serializers.ModelSerializer):

    class Meta:

        model = Course
        fields = (
            'id',
            'title',
            'url',
            'create',
            'active',
            'assessments',
            #'get_media_assessments'
        )

    def get_media_assessments(self, obj):
        media = obj.assessments.aggregate(Avg('assessment')).get('assessment__avg')

        if media is None:
            return 0
        return (media * 2) / 2

