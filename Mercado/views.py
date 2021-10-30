from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from Mercado.serializer import mallSerializer, tiendaSerializer, productoSerializer
from Mercado.models import mall, tienda, producto

# Create your views here.


class mallViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = mall.objects.all()
    serializer_class = mallSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', '=id']

class tiendaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = tienda.objects.all()
    serializer_class = tiendaSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', '=mall__id', '=mall__nombre']

class productoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = producto.objects.all()
    serializer_class = productoSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', '=tienda__id']