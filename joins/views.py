from django.shortcuts import render

# Create your views here.
def joins_home(request):
	return render(request, 'joins_index.html')