from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import CourseSerializer, AssessmentSerializer
from .models import Course, Assessment


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get'])
    def assessments(self, request, pk=None):
        self.pagination_class.page_size = 1
        assessments = Assessment.objects.filter(course_id=pk)
        page = self.paginate_queryset(assessments)

        if page is not None:
            serializer = AssessmentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AssessmentSerializer(assessments, many=True)
        return Response(serializer.data)


class AssessmentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
