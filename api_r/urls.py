from django.urls import path
from api_r.views import lista_consulta

urlpatterns = [
    path('lista_consulta', lista_consulta, name="lista_consulta")
]
