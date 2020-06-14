from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes


# Create your views here.
@api_view(['GET'])
@renderer_classes([JSONRenderer])
def ping_response(request):
    return Response(True,status=200)