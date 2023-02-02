from django import template

register = template.Library()


@register.filter
def remove_dashes(value):
    return value.replace("-", " ")
