from Mercado.models import mall, tienda, producto
from rest_framework import serializers

class mallSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = mall
        fields = '__all__'

class tiendaSerializer(serializers.HyperlinkedModelSerializer):
    datos_mall = mallSerializer(source = "mall", read_only=True)
    class Meta:
        model = tienda
        fields = '__all__'

class productoSerializer(serializers.HyperlinkedModelSerializer):
    datos_tienda = tiendaSerializer(source = "tienda", read_only=True)
    class Meta:
        model = producto
        fields = '__all__'