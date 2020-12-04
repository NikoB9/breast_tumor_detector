# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	"""return HttpResponse('<h1>Hello, Welcome to this test</h1>')"""

	"""Le chemin des templates est renseigne dans "DIRS" de "TEMPLATES" dans settings.py
	DONC PAS BESOIN DE RENSEIGNER LE CHEMIN ABSOLU"""
	return render(request, "index.html")


def us(request):
	return render(request, "us.html")

def algoSVM(request):
	return render(request, "algoSVM.html")

def algoKNN(request):
	return render(request, "algoKNN.html")

def algoRandomForest(request):
	return render(request, "algoRandomForest.html")

def breastCancer(request):
	return render(request, "breastCancer.html")



def handler404(request, exception):
	return render(request, "errors/404.html")

def handler500(request):
	return render(request, "errors/500.html")
