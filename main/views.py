from django.shortcuts import render

from main.forms import *


def index(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
    return render(request, 'order.html', {'form': form})