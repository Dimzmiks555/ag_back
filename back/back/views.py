from http.client import HTTPResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Etalon
from .serializers import EtalonSerializer


class EtalonViewSet(viewsets.ModelViewSet):
    queryset  = Etalon.objects.all()
    serializer_class  = EtalonSerializer