from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet
from .views import FuncionarioViewSet


router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'Funcionarios', FuncionarioViewSet)
urlpatterns = [
    path('', include(router.urls)),
]


