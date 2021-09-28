from django.contrib.admin import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django.shortcuts import render

from api.serializers import PoverkiSerializer
from api.models import Poverka


class PoverkaViewSet(ModelViewSet):
    queryset = Poverka.objects.all()
    serializer_class = PoverkiSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['mit_title']
    search_fields = ['mit_number', 'mi_number']
    ordering_fields = ['mit_number', 'mi_number', 'applicability']

def auth(request):
    return render(request, 'oauth.html')
