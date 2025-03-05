from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Task.objects
    serializer_class = TaskSerializer
