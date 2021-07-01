from django import template

register = template.Library()


@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name='add_value')
def add_value(value, arg):
    return value.as_widget(attrs={'value': arg})

@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)
