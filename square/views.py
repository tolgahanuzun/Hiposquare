from django.shortcuts import render
from django.template import Template, Context, RequestContext
from django.http import *   
from square.models import Square
import requests
import json



def search(request):
	'''Producing results using Api'''

	client_id = 'xxx'
	client_secret = 'xxx'

	try:
		locations = request.GET['locations']
		looking_for = request.GET['looking']
		url = 'https://api.foursquare.com/v2/venues/search?near=' + locations +'&query=' + looking_for +'&client_id=' + client_id + '&client_secret=' + client_secret +'&v=20150728'
		rget = requests.get(url)
		data = rget.json()['response']['venues']

		logtime = Square(looking_for=looking_for, locations=locations)
		logtime.save()

		recent = Square.objects.order_by('-date')[:20]

		return render(request, 'details.html', {'contexts': data, 'recents': recent})

	except:
		return render(request, 'base.html', {'error': 'Error'})

def base(request):
	'''Home Producer'''

	if request.method == "GET":
		recent = Square.objects.order_by('-date')[:20]

		return render(request, 'base.html', {'recents': recent})
	else:
		return render(request, 'base.html', {'error': 'Error'})

