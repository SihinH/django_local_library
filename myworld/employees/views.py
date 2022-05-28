from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Employees

def index(request):
  myemployees = Employees.objects.all().values()
  template = loader.get_template('indexe.html')
  context = {
    'myemployees': myemployees,
  }
  return HttpResponse(template.render(context, request))
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))