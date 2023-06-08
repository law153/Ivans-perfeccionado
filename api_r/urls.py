from django.urls import path
from api_r.views import lista_consulta, lista_detalle, detalle_detalle, detalle_consulta

urlpatterns = [
    path('lista_consulta', lista_consulta, name="lista_consulta"),
    path('lista_detalle', lista_detalle, name="lista_detalle"),
    path('detalle_detalle/<id>', detalle_detalle, name='detalle_detalle'),
    path('detalle_consulta/<id>', detalle_consulta, name='detalle_consulta'),
]
