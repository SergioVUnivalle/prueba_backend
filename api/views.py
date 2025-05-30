from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import Municipio
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Centroid
from core.models import Oficina, Municipio
from rest_framework_gis.serializers import GeoFeatureModelSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def municipios_por_departamento(request):
    departamento = request.GET.get('departamento')
    municipios = Municipio.objects.filter(dpto__iexact=departamento).values_list('municipio', flat=True).distinct()
    return Response({'municipios': list(municipios)})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def geometria_municipio_por_oficina(request, oficina_id):
    try:
        oficina = Oficina.objects.get(id=oficina_id)
        punto = oficina.shape
        municipio = Municipio.objects.get(shape__contains=punto)
        geojson = {
            "type": "Feature",
            "geometry": municipio.shape.geojson,
            "properties": {
                "municipio": municipio.municipio,
                "dpto": municipio.dpto
            }
        }
        return Response(geojson)
    except (Oficina.DoesNotExist, Municipio.DoesNotExist):
        return Response({'error': 'Oficina o municipio no encontrado'}, status=404)