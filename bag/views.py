from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product
from products.models import Wishlist
from products.models import GiftCard
from django.contrib.auth.decorators import login_required
from bag.contexts import bag_contents
from decimal import Decimal


def view_bag(request):
    """ A view that renders the bag contents page """

    bag_data = bag_contents(request)

    total = bag_data['total']
    discount = bag_data.get('discount', Decimal('0.00'))
    delivery = bag_data.get('delivery', Decimal('0.00'))

    gift_card_amount = Decimal(request.session.get('gift_card_amount', 0))
    gift_card_code = request.session.get('gift_card_code')

    grand_total = total - discount + delivery - gift_card_amount
    if grand_total < 0:
        grand_total = Decimal('0.00')

    context = {
        'bag_items': bag_data['bag_items'],
        'total': total,
        'product_count': bag_data['product_count'],
        'discount': discount,
        'delivery': delivery,
        'free_delivery_delta': bag_data['free_delivery_delta'],
        'gift_card_amount': gift_card_amount,
        'gift_card_code': gift_card_code,
        'grand_total': grand_total,
    }

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')

        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    bag = request.session.get('bag', {})

    item_id = str(item_id)
    if item_id in bag:
        del bag[item_id]
        request.session['bag'] = bag
        messages.success(request, "Item removed from your bag.")

    return redirect('view_bag')


def add_wishlist_to_bag(request, item_id):
    # Get the product by ID
    product = get_object_or_404(Product, pk=item_id)

    # Add to bag (session)
    bag = request.session.get('bag', {})
    product_id = str(product.id)

    if product_id in bag:
        bag[product_id] += 1
    else:
        bag[product_id] = 1

    request.session['bag'] = bag

    # Remove from wishlist for this user
    Wishlist.objects.filter(user=request.user, product=product).delete()

    # Success message
    messages.success(request, f"{product.name} was added to your bag.")

    # Stay on wishlist page
    return redirect('view_wishlist')

@login_required
def apply_gift_card(request):
    if request.method == 'POST':
        code = request.POST.get('gift_card_code')
        try:
            gift_card = GiftCard.objects.get(code=code, is_used=False)
            request.session['gift_card_amount'] = str(gift_card.value)
            request.session['gift_card_code'] = gift_card.code
            messages.success(request, f"Gift Card '{code}' applied: £{gift_card.value} off!")
        except GiftCard.DoesNotExist:
            messages.error(request, "Invalid or already used Gift Card.")

    return redirect('view_bag')
