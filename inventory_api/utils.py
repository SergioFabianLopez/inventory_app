from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if response.status_code == status.HTTP_400_BAD_REQUEST:
            response.data = {
                'error': 'Error de validación',
                'detail': response.data
            }
        elif response.status_code == status.HTTP_404_NOT_FOUND:
            response.data = {
                'error': 'Recurso no encontrado',
                'detail': 'El recurso solicitado no existe.'
            }
        elif response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
            response.data = {
                'error': 'Error interno del servidor',
                'detail': 'Ocurrió un error inesperado en el servidor.'
            }
        logger.error(f"Error en la API: {response.status_code} - {response.data}", exc_info=True)
    else:
        logger.error(f"Error inesperado: {exc}", exc_info=True)
        response = Response(
            {'error': 'Error interno del servidor', 'detail': 'Ocurrió un error inesperado.'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return response
