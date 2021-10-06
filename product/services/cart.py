from django.db import models

from product.models import Product, CartProduct


def add_to_cart(slug_product, user, cart):
    product = Product.objects.filter(slug=slug_product).first()
    cart_product, created = CartProduct.objects.get_or_create(
        user=user, cart=cart, product=product
    )
    if created:
        cart.products.add(cart_product)
    save_cart(cart)


def save_cart(cart):
    """An analogue of the `save ()` method"""
    cart_product = cart.products.aggregate(models.Sum('all_price'), models.Sum('count'))
    count = cart_product['count__sum']
    if cart_product.get('all_price__sum'):
        if count >= 3 and count <= 5:
            cart.discount = cart_product['all_price__sum'] - (cart_product['all_price__sum'] * 5) / 100
            cart.all_price = 0
        elif count > 5:
            cart.discount = cart_product['all_price__sum'] - (cart_product['all_price__sum'] * 10) / 100
            cart.all_price = 0
        else:
            cart.all_price = cart_product['all_price__sum']
            cart.discount = 0
    else:
        cart.discount = 0
        cart.all_price = 0

    cart.all_product = cart_product['count__sum']
    cart.save()


def delete_from_cart(slug_product, user, cart):
    product = Product.objects.filter(slug=slug_product).first()
    cart_product = CartProduct.objects.get(
        user=user, cart=cart, product=product
    )
    cart.products.remove(cart_product)
    cart_product.delete()
    save_cart(cart)


def change_count_cart_product(slug_product, user, cart, count):
    product = Product.objects.filter(slug=slug_product).first()
    cart_product = CartProduct.objects.get(
        user=user, cart=cart, product=product
    )

    count = int(count)
    cart_product.count = count
    cart_product.save()
    save_cart(cart)


def check_correct_basket(cart):
    """This method checks all products for stock"""
    for i in cart.products.all():
        if i.product.quantity_in_stock == 0:
            cart.products.remove(i)
            i.delete()
    save_cart(cart)
    return cart
