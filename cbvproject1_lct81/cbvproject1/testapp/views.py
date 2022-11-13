from django.views.generic import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
class HelloWorldView(View):
    def get(self, request):
        return HttpResponse('<h1>This is form class base view </h1>' )

class HelloworldTemplateView(TemplateView):
    template_name='testapp/results.html'

class HelloWorldContextTemplate(TemplateView):
    template_name='testapp/info.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='Amol'
        context['subject']='python'
        context['marks']=100
        return context