from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import viewsets


router_v1 = SimpleRouter()
router_v1.register("tasks", viewsets.TaskViewSet, "tasks")

urlpatterns = [
    path("", include(router_v1.urls))
]
