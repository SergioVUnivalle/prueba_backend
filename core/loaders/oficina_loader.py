from django.contrib.gis.utils import LayerMapping
from core.models import Oficina

oficina_mapping = {
    'nombre': 'nombre',
    'gid': 'gid',
    'departamen': 'departamen',
    'municipio': 'municipio',
    'geom': 'Point',
}

def cargar_oficinas(shp_path):
    lm = LayerMapping(
        Oficina,
        shp_path,
        oficina_mapping,
        transform=False,
        encoding='utf-8'
    )
    lm.save(strict=True, verbose=True)
