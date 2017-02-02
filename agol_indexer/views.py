from django.shortcuts import render
from django.http import HttpResponse, Http404

def index_home(request):
	return render(request, 'index.html')