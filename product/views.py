from django.shortcuts import render, get_object_or_404
from product.models import *
from cart.forms import CartAddProductForm
from django.views.generic import TemplateView, ListView, DetailView


class IndexView(TemplateView):
    template_name = 'index.html'


class CategoriesView(ListView):
    model = Product
    template_name = 'categories.html'


class CheckView(TemplateView):
    template_name = 'check-out.html'


class ThankView(TemplateView):
    template_name = 'thank.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class ProductView(DetailView):
    model = Product
    form = Product
    template_name = 'product-page.html'


class CartView(TemplateView):
    template_name = 'shopping-cart.html'


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
        'form': CartAddProductForm
    }
    return render(request, 'product-page.html', context)
