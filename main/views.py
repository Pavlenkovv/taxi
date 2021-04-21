from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render

from main.forms import *
from main.models import *


def index(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # check for available cars
            car = Car.objects.filter(is_ordered=False)[:1]
            if not car:
                return render(request, 'order.html', {'form': form, 'no_car': True})
            car[0].is_ordered = True
            car[0].save()
            order = Order(customer_name=form.cleaned_data['customer_name'],
                          customer_phone=form.cleaned_data['customer_phone'],
                          address_from=form.cleaned_data['address_from'],
                          address_to=form.cleaned_data['address_to'],
                          in_what_time=form.cleaned_data['in_what_time'],
                          car=car[0])
            order.save()
            return HttpResponseRedirect(f"/details?id={order.id}")

    return render(request, 'order.html', {'form': form})


def user_order_details(request):
    order_id = request.GET.get('id')
    order = Order.objects.get(pk=order_id)
    return render(request, 'order_details.html', {'order': order})


@login_required
def order_list(request):
    page = request.GET.get('page', 1)
    order_list = Order.objects.all()
    paginator = Paginator(order_list, 3)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    return render(request, 'order_list.html', {'orders': orders})


@login_required
def order_details(request):
    order_id = request.GET.get('id')
    order = Order.objects.get(pk=order_id)
    if request.method == 'POST':
        if order.car is not None:
            order.car.is_ordered = False
            order.car.save()
        order.order_done = True
        order.save()
    return render(request, 'order_details.html', {'order': order})
