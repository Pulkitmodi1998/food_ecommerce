# store/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return value * arg
    except (ValueError, TypeError):
        return ''

@register.filter
def total_price(cart_items):
    return sum(item.quantity * item.product.price for item in cart_items)
