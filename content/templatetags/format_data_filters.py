from __future__ import division

from django.template.defaulttags import register


@register.filter
def format_date(date):
    return str(date).replace('-', '/')


@register.filter
def split_by(value, symbol):
    return value.split(symbol)


@register.filter
def no_last(value, count):
    # return sentence without last 'count' (1,2 etc) words
    return " ".join(value.split(' ')[:-int(count)])


@register.filter
def latest(value, count):
    # return lastest 'count' (1, 2, 3 etc) words
    return " ".join(value[-int(count):])


@register.filter
def split_by_nth(value, n):
    return  [value[i:i+n] for i in range(0, len(value), n)]


@register.filter
def filesize(value):
    try:
        size = value.size
    except Exception as e:
        # if file not exists
        size = 0
    return "%.2f" % (int(size) / 1000000)
