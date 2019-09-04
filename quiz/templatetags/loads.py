from django import template
register=template.Library()
@register.filter(name='changeval')
def changeval(val):
    return val+2