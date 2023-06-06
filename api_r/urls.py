from django.urls import path
from api_r.views import lista_consulta, lista_detalle

urlpatterns = [
    path('lista_consulta', lista_consulta, name="lista_consulta"),
    path('lista_detalle', lista_detalle, name="lista_detalle")
]
