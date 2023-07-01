from django import forms
from apps.tipocuenta.models import TipoCuenta

class TipoCuentaForm (forms.ModelForm):
    class Meta:
        model = TipoCuenta
        fields = [
            'descripcion',
        ]
        labels ={
            'descripcion': 'Descripcion',
        }
        Widgets={
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
        }
