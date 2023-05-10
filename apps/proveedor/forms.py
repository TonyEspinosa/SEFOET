from django.forms import ModelForm
from .models import m_proveedor

class fm_proveedor(ModelForm):
    class Meta:
        model = m_proveedor
        #fields = '__all__'
        fields = ['nombre'
                  , 'categoria'
                  , 'tipo'
                  , 'descripcion'
                  , 'contacto'
                  , 'puesto'
                  , 'email'
                  , 'tel1']
