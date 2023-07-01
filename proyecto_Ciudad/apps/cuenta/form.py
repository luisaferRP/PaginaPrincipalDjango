from django import forms
from apps.cuenta.models import Cuenta

class CuentaForm (forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = [
            'nombre_cuenta',
            'fecha_apertura',
            'salario',
            'tipocuenta',
      
        ]
        labels ={
            'nombre_cuenta': 'Nombre de la Cuenta',
            'fecha_apertura': 'Fecha de Apertura',
            'salario': 'Salario',
            'tipocuenta': 'Tipo de Cuenta',

        }
        Widgets={
            'nombre_cuenta': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_apertura': forms.TextInput(attrs={'class':'form-control'}),
            'salario': forms.TextInput(attrs={'class':'form-control'}),
            'tipocuenta': forms.Select(attrs={'class':'form-control'}),

        }
