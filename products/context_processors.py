from users.models import Basket


def basket(request):
    user = request.user
    return {'basket_list': Basket.objects.filter(user=user) if user.is_authenticated else []}
