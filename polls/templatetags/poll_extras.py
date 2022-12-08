from django import template
from django.template.defaultfilters import floatformat
from ..models import Choice
from django.db.models import Sum
register = template.Library()


# @register.filter
# def percent(part):
#     Choice.votes.all().aggregate = whole = (sum('sum'))
#     try:
#         return "%d%%" % (float(part) / whole * 100)
#     except (ValueError, ZeroDivisionError):
#         return ""


# @register.filter
# def percent(value):
#     max = Choice.votes.count()
#     return '{0:.2%}'.format(value)

@register.filter
def percent(part, whole):
    Choice.votes.aggregate(whole=Sum('votes'))
    try:
        return "%d%%" % (float(part) / whole * 100)
    except (ValueError, ZeroDivisionError):
        return ""
