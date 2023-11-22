import django_filters

from .models import *

class ProveedorFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains', label=' Nombre')
    descripcion = django_filters.CharFilter(lookup_expr='icontains', label=' Descripción')
    contacto = django_filters.NumberFilter(lookup_expr='icontains', label=' Contacto')

    class meta:
        model = m_proveedor
        fields = ['nombre', 'descripcion', 'contacto']
        groups = [
            CombinedGroup(filters=['first_name', 'last_name'], combine=operator.or_),
        ]