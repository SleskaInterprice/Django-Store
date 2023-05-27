from django.shortcuts import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from orders.forms import OrderForm
from orders.models import Orders


class CreateOrderView(CreateView):
    template_name = 'orders/order-create.html'
    model = Orders
    form_class = OrderForm

    def get_success_url(self):
        return reverse('orders:create_order')

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(CreateOrderView, self).form_valid(form)


class Success(TemplateView):
    template_name = 'orders/success.html'
