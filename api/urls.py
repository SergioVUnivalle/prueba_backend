from .views import municipios_por_departamento, geometria_municipio_por_oficina
from django.urls import path

urlpatterns = [
    path('municipios/', municipios_por_departamento),
    path('municipio-por-oficina/<int:oficina_id>/', geometria_municipio_por_oficina),
]