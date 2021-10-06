from product.models import Product


def get_auto_name(category_slug):
    """Автоматичні імена, для пошуку"""
    qs = Product.objects.filter(category__slug=category_slug).values_list('title', flat=True)
    return list(qs)
