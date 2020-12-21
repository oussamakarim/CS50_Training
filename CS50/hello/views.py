from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def home(request):
	return render(request, "hello/site.html");


def test(request):
	now = datetime.datetime.now()
	return render(request, "hello/index.html", {
		"newyear": now.month==8 and now.day==20
		});

def greet(request, name):
	return render(request, "hello/greet.html",{
		"name" : name
		})