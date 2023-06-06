from rest_framework import serializers
from core.models import Detalle, Consulta

class consultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['id_consulta','nombre_consultante','asunto_consulta','mensaje_consulta']


class detalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle
        fields = ['id_detalle','cantidad','subtotal','venta','producto']