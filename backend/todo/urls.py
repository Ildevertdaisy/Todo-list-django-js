
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.api.viewsets import TodoViewSet

router = DefaultRouter()

router.register("todos", TodoViewSet, basename="todos")

urlpatterns = [
    path("api/", include(router.urls))
]