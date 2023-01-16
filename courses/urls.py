
from .views import AssessmentViewSet, CourseViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('avaliacoes', AssessmentViewSet)
router.register('cursos', CourseViewSet)
