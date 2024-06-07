import datetime
from django import template

register = template.Library()

#costum filter tag
@register.filter
def cutter(value, args):
    return value[:args]

#costum simple template tag
@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

