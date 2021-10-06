def calc_quantity_in_stock(cart_products):
    for i in cart_products:
        i.product.quantity_in_stock -= i.count
        i.product.save()
