from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    """
    Custom global DRF exception handler
    """
    response = exception_handler(exc, context)

    if response is not None:
        response.data = {
            "success": False,
            "error": {
                "type": exc.__class__.__name__,
                "details": response.data,
            }
        }

    return response
