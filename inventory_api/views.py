from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Menu
from .serializers import MenuSerializer
import logging

logger = logging.getLogger(__name__)


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        logger.info(f"Item creado: {serializer.data['name']}")
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        logger.info(f"Item recuperado: {instance.name}")
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        logger.info(f"Item actualizado: {instance.name}")
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        logger.info(f"Item eliminado: {instance.name}")
        return Response(status=status.HTTP_204_NO_CONTENT)

    def handle_exception(self, exc):
        logger.error(f"Error en la API de Alimentos/Bebidas: {exc}",
                     exc_info=True)
        return super().handle_exception(exc)
