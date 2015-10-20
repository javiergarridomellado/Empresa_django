# Create your views here.
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.template import RequestContext

class index(TemplateView):
	
	def get(self, request, *args, **kwargs):
		return render_to_response('emp/index.html',
			context_instance = RequestContext(request))
		

class index2(TemplateView):
	template_name = 'emp/index2.html'

