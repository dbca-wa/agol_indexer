from django.shortcuts import render
from django.http import HttpResponse, Http404

def viewer_home(request):
	return render(request, 'viewer.html')