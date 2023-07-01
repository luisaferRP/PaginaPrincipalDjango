from django.shortcuts import render
from django.http import HttpResponse
from apps.tipocuenta.models import TipoCuenta
from apps.tipocuenta.form import TipoCuentaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request, "cuenta/index.html")

class TipoCuentaList(ListView):
    model=TipoCuenta
    template_name='tipocuenta/tipo_list.html'


class TipoCuentaCreate(CreateView):
    model=TipoCuenta
    form_class= TipoCuentaForm
    template_name='tipocuenta/tipo_form.html'
    success_url= reverse_lazy('tipo_listar')


class TipoCuentaEdit(UpdateView):
    model=TipoCuenta
    form_class= TipoCuentaForm
    template_name='tipocuenta/tipo_form.html'
    success_url= reverse_lazy('tipo_listar')


class TipoCuentaDelete(DeleteView):
    model=TipoCuenta
    template_name='tipo/tipo_delete.html'
    success_url= reverse_lazy('tipo_listar')
