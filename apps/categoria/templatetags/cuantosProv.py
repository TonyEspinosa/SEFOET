from django import template
register = template.library()

from apps.proveedor.models import m_proveedor
#from apps.categoria.models import m_categoria

@register.tag
def cuantosProv(item):
        return m_proveedor.objects.filter(categoria=item).count()