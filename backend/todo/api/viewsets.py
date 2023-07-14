
from rest_framework.viewsets import ModelViewSet
from todo.api.serializers import TodoSerializer
from todo.models import Todo


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
