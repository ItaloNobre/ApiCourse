from .views import AssessmentViewSet, CourseViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('assessments', AssessmentViewSet)
router.register('courses', CourseViewSet)
