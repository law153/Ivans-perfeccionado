from django.urls import path,include
from .views import mostrarIndex,mostrarNosotros

urlpatterns = [
    path('',mostrarIndex,name="mostrarIndex"),
    path('nosotros/',mostrarNosotros,name="mostrarNosotros"),
]
