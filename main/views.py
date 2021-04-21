from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from main.forms import *
from main.models import *


def index(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
    return render(request, 'order.html', {'form': form})


@login_required
def order_list(request):
    page = request.GET.get('page', 1)
    order_list = Order.objects.all()
    paginator = Paginator(order_list, 10)
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
    return render(request, 'order_details.html', {'order': order})