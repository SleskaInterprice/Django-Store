from django.shortcuts import render


products_list = [
    {
        'image': 'vendor/img/products/Adidas-hoodie.png',
        'name': 'Худи черного цвета с монограммами adidas Originals',
        'price': 6090,
        'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
    },
    {
        'image': 'vendor/img/products/Blue-jacket-The-North-Face.png',
        'name': 'Синяя куртка The North Face',
        'price': 23725,
        'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
    },
    {
        'image': '/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
        'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
        'price': 3390,
        'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
    },
    {
        'image': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
        'name': 'Черный рюкзак Nike Heritage',
        'price': 2340,
        'description': 'Плотная ткань. Легкий материал.',
    },
    {
        'image': 'vendor/img/products/Black-Dr-Martens-shoes.png',
        'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
        'price': 13590,
        'description': 'Гладкий кожаный верх. Натуральный материал.',
    },
    {
        'image': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
        'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
        'price': 2890,
        'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
    },
]


def index(request):
    return render(request, template_name='products/index.html')


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products_list': products_list,
    }
    return render(request, template_name='products/products.html', context=context)
