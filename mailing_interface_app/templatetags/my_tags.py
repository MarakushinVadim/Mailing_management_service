from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return (f"/media/{path}")
    return "#"


@register.filter()
def description_filter(description):
    if len(description) > 100:
        return f'{description[:97]}...'
    return description


