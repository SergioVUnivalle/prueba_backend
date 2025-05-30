from django.core.management.base import BaseCommand
from core.loaders.municipio_loader import cargar_municipios
from core.loaders.oficina_loader import cargar_oficinas

class Command(BaseCommand):
    help = "Carga los shapefiles de municipios y oficinas"

    def add_arguments(self, parser):
        parser.add_argument('--municipios', type=str, help='Ruta al shapefile de municipios')
        parser.add_argument('--oficinas', type=str, help='Ruta al shapefile de oficinas')

    def handle(self, *args, **kwargs):
        municipios_shp = kwargs['municipios']
        oficinas_shp = kwargs['oficinas']

        if municipios_shp:
            self.stdout.write("Cargando municipios")
            cargar_municipios(municipios_shp)
        
        if oficinas_shp:
            self.stdout.write("🏢 Cargando oficinas")
            cargar_oficinas(oficinas_shp)

        self.stdout.write(self.style.SUCCESS("✔️ Carga completada."))
