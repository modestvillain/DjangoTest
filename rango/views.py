from django.shortcuts import render
from django.http import HttpResponse

# A view called index
# A view takes in at least one argument
def index(request):
	return HttpResponse("Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")