from django.shortcuts import render
from django.http import HttpResponse
from apps.cuenta.models import Cuenta
from apps.cuenta.form import CuentaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

def index(request):
    return render(request, "cuenta/index.html")

class CuentaList(ListView):
    model=Cuenta
    template_name='cuenta/cuenta_list.html'


class CuentaCreate(CreateView):
    model=Cuenta
    form_class= CuentaForm
    template_name='cuenta/cuenta_form.html'
    success_url= reverse_lazy('cuenta_listar')


class CuentaEdit(UpdateView):
    model=Cuenta
    form_class= CuentaForm
    template_name='cuenta/cuenta_form.html'
    success_url= reverse_lazy('cuenta_listar')


class CuentaDelete(DeleteView):
    model=Cuenta
    template_name='cuenta/cuenta_delete.html'
    success_url= reverse_lazy('cuenta_listar')