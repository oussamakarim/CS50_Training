from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import flight,Passenger

# Create your views here.

def index(request):
	return render(request, "flights/index.html", {
		"flights": flight.objects.all()
		})

def flight1(request, flight_id):
	Flight = flight.objects.get(pk= flight_id)
	return render(request, "flights/flight.html", {
		"flight": Flight,
		"passengers": Flight.passengers.all(),
		"non_passengers": Passenger.objects.exclude(flights=Flight).all()
	})

def book(request, flight_id):
	if request.method == "POST":
		Flight = flight.objects.get(pk=flight_id)
		passenger = Passenger.objects.get(pk = int(request.POST["passenger"]))
		passenger.flights.add(Flight)
		return HttpResponseRedirect(reverse("flight", args=(Flight.id,)))