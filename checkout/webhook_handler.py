from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Product

import json
import time


class StripeWH_Handler:
    """Handle Stripe Webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent_succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        # Store the billing and delivery details
        billing_details = intent.charges.data[0].billing_details
        delivery_details = intent.delivery_details
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clear data in the delivery details
        for field, value in delivery_details.address.items():
            if value == "":
                delivery_details.address[field] = None

        # If there is no order already in the database
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get (
                    full_name__iexact=delivery_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=delivery_details.number,
                    country__iexact=delivery_details.address.country,
                    postcode__iexact=delivery_details.address.postal_code,
                    town_or_city__iexact=delivery_details.address.town_or_city,
                    street_address1__iexact=delivery_details.address.line1,
                    street_address2__iexact=delivery_details.address.line2,
                    county__iexact=delivery_details.address.county,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,           
                )
                # If there is an order already in the database
                order_exists = True
                break
            except Order.DoesNotExist:
                attemp += 1
                time.sleep(1)
            if order_exists:
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                    status=200)
            else:
            # If there is no order in the databse
                order = None
                try:
                    order = Order.objects.create(
                        full_name=delivery_details.name,
                        email=billing_details.email,
                        phone_number=delivery_details.number,
                        country=delivery_details.address.country,
                        postcode=delivery_details.address.postal_code,
                        town_or_city=delivery_details.address.town_or_city,
                        street_address1=delivery_details.address.line1,
                        street_address2=delivery_details.address.line2,
                        county=delivery_details.address.county,
                        original_basket=basket,
                        stripe_pid=pid,
                    )
                    for item_id, item_data in json.loads(basket).items():
                        product = Product.objects.get(id=item_id)
                        if isinstance(item_data, int):
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=item_data,
                            )
                            order_line_item.save()
                        else:
                            for size, quantity in item_data['items_by_size'].items():
                                order_line_item = OrderLineItem(
                                    order=order,
                                    product=product,
                                    quantity=quantity,
                                    product_size=size,
                                )
                                order_line_item.save()
                except Exception as e:
                    if order:
                        order.delete()
                    return HttpResponse(
                        content=f'Webhook received: {event["type"]} | ERROR: {e}',
                        status=500)

            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
