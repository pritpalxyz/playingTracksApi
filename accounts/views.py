from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def index(request):
	html = "<html><body>INTERNAL SERVER ERROR</html>"
	return HttpResponseRedirect('http://www.google.com/')
