from django.views.generic import CreateView, TemplateView, ListView
from .models import Empresa
from django.core.urlresolvers import reverse_lazy

class RegistrarEmpresa(CreateView):
	template_name = 'empresas/registrarEmpresa.html'
	model = Empresa
	success_url = reverse_lazy('redirigir_empresa')


class RedirigirEmpresa(ListView):
	template_name = 'empresas/redirigirEmpresa.html'
	model = Empresa
	context_object_name = 'empresas'
		