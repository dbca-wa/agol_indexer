from django.shortcuts import render
from django.http import HttpResponse, Http404

def index_home(request):
	return render(request, 'home_search.html')