from  . models import Cart,CartItem
from  . views import  _cart_id

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=_cart_id(request))
            car_items=CartItem.objects.all().filter(cart=cart[:1])
            for car_items in car_items:
                item_count += car_items.quantity
        except Cart.DoseNotExist:
            item_count = 0
    return  dict(item_count=item_count)