import re, os
from django import template

register = template.Library()



@register.assignment_tag
def re_search(pattern, strvar, flags=0):
    return re.search(pattern, strvar, flags)


@register.assignment_tag
def re_match(pattern, strvar,  flags=0):
    return re.match(pattern, strvar,  flags)


@register.assignment_tag
def re_split(pattern, strvar, maxsplit=0, flags=0):
    res = re.split(pattern, strvar, maxsplit, flags)
    return res

@register.assignment_tag
def re_findall(pattern, strvar,  flags=0):
    return re.split(pattern, strvar, flags)

@register.assignment_tag
def re_sub(pattern, repl, strvar, count=0, flags=0):
    return re.sub(pattern, repl, strvar, count, flags)


@register.assignment_tag
def re_subn(pattern, repl, strvar, count=0, flags=0):
    return re.sub(npattern, repl, strvar, count, flags)


@register.assignment_tag
def re_escape(strvar):
    return re.escape(strvar)


@register.filter
def replace_ext(filename, newext):
    base, ext = os.path.splitext(filename)
    return "{}1.{}".format(base, newext)