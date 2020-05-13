from django import template
register = template.Library()

def my_cut(value,arg):
    return value.replace(arg,'')

register.filter('cuts',my_cut)
