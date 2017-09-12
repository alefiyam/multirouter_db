# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Product
from django.views.generic.edit import CreateView
from .models import Database
from django.http import HttpResponseRedirect
from django.views.generic import ListView

# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating


@login_required(login_url='/login/')
def home(request):
    user = request.user
    databases = user.databases.all()
    context = {'databases': databases}
    return render(request, "product/dashboard.html", context)


class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'price']

    def get_context_data(self, **kwargs):
        context = super(ProductCreate, self).get_context_data(**kwargs)
        context['databases'] = self.request.user.databases.all()
        return context

    def post(self, request):
        user_id = request.user.id
        database_id = request.POST.get('database', None)
        database_obj = Database.objects.get(pk=database_id)
        item_name = request.POST.get('name', None)
        item_price = request.POST.get('price', None)
        if database_obj:
            product_obj = Product.objects.using(database_obj.name).create(
                name=item_name, price=item_price, user_id=user_id)
            return HttpResponseRedirect('/home/')

        return render(request, 'product/product_form.html',
                      {'form': self.get_form()})


class ProductList(ListView):

    model = Product
    template_name = 'product/product_list.html'

    def get_context_data(self, **kwargs):
        product_list = []
        context = super(ProductList, self).get_context_data(**kwargs)
        databases = self.request.user.databases.all()
        for database_obj in databases:
            products = Product.objects.using(
                database_obj.name).filter(user_id=self.request.user.id)
            product_list.append(products)
        context['product_list'] = product_list
        return context
