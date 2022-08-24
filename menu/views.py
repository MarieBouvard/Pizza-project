from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.

def index(request):
    # pizzas = Pizza.objects.all()
    # pizzas = [pizza.nom + " : " + str(pizza.prix) + " €" for pizza in pizzas]
    # pizzas_str = ", ".join(pizzas)
    # return HttpResponse("Les pizzas " + pizzas_str + ".")
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, 'menu/index.html', {'pizzas': pizzas})