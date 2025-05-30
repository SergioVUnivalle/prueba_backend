from django.contrib.gis.utils import LayerMapping
from core.models import Municipio

municipio_mapping = {
    'municipio': 'MUNICIPIO',
    'dpto': 'DPTO',
    'disposicion': 'DISPOSICIO',
    'cod_dane': 'COD_DANE',
    'geom': 'Geometry',
}

def cargar_municipios(shp_path):
    lm = LayerMapping(
        Municipio,
        shp_path,
        municipio_mapping,
        transform=False,
        encoding='utf-8'
    )
    lm.save(strict=True, verbose=True)
