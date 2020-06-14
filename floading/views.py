from .models import endereco
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from .serializers import enderecoSerializer
from .scraping import scraping
import logging
import json

# Create your views here.

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def endereco_list_APIview(request):
    data_retriever = scraping.matcher()
    data = data_retriever.retrieve()
    json_data = json.dumps(data,indent=4,sort_keys=True,ensure_ascii=False)
    return Response(json_data,status=200,)

