from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.conf import settings
from products.models import Product

def bag_contents(request):
    bag_items = []
    total = Decimal('0.00')
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        line_total = product.price * quantity
        total += line_total
        product_count += quantity

        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'line_total': line_total,
        })

    # Custom bulk discount logic, 5% discount
    discount = Decimal('0.00')
    discount_threshold = 3
    discount_rate = Decimal('0.05')

    if product_count >= discount_threshold:
        discount = total * discount_rate

    discounted_total = total - discount

    # Delivery calculated after the discount
    if discounted_total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = discounted_total * Decimal(
            settings.STANDARD_DELIVERY_PERCENTAGE / 100
        )
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - discounted_total
    else:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')

    # Gift Card
    gift_card_amount = Decimal(request.session.get('gift_card_amount', 0))

    # Grand total including delivery and subtracting gift card
    grand_total = discounted_total + delivery - gift_card_amount
    if grand_total < 0:
        grand_total = Decimal('0.00')  # prevent negative totals

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'discount': discount,
        'discount_threshold': discount_threshold,
        'discount_rate': discount_rate,
        'discounted_total': discounted_total,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'gift_card_amount': gift_card_amount,
    }

    return context
