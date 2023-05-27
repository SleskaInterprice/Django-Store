from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect

from baskets.models import Basket
from products.models import Product


@login_required
def add_product(request, product_id=None, quantity=1):
    product = Product.objects.get(id=product_id)
    user_basket = Basket.objects.filter(user=request.user, product=product)
    if not user_basket.exists():
        basket = Basket(user=request.user, quantity=1, product=product)
        basket.save()
    else:
        user_basket = user_basket.first()
        user_basket.quantity += quantity
        user_basket.save()
    return HttpResponseRedirect(redirect_to=request.META['HTTP_REFERER'])


@login_required
def delete_basket(request, basket_id):
    basket = Basket.objects.filter(id=basket_id)
    if basket.exists():
        basket.first().delete()
    return HttpResponseRedirect(redirect_to=request.META['HTTP_REFERER'])
