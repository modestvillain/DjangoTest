from django.shortcuts import render
from django.http import HttpResponse

# A view called index
# A view takes in at least one argument
def index(request):
	return HttpResponse('<a href="/rango/">Index</a>')
	# return HttpResponse("IT'S AN ABOUT PAGE NOW!")