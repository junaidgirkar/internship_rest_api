from django.urls import path, include
from webapp.views import JobViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("jobs", JobViewSet, basename="job")
urlpatterns = router.urls
