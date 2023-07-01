from django import forms
from apps.cliente.models import Cliente

class ClienteForm (forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'cedula',
            'nombre_cliente',
            'apellido_cliente',
            'telefono_cliente',
            'direccion_cliente',
            'cuenta',

        ]
        labels ={
            'cedula':'Cedula',
            'nombre_cliente': 'Nombre',
            'apellido_cliente': 'Apellido',
            'telefono_cliente': 'Telefono',
            'direccion_cliente': 'Dirección',
            'cuenta':'Cuenta',

        }
        Widgets={
            'cedula': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_cliente': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_cliente': forms.TextInput(attrs={'class':'form-control'}),
            'Telefono_cliente': forms.TextInput(attrs={'class':'form-control'}),
            'direccion_cliente': forms.TextInput(attrs={'class':'form-control'}),
            'cuenta': forms.Select(attrs={'class':'form-control'}),
        }
