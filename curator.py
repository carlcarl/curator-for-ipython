#!/usr/bin/env python
# encoding: utf-8

import json
import urllib2
from IPython.core.display import HTML

# Set your token here
token = ''

url = 'http://curator.im/api/'
warn_html = HTML('<p>Illegal command!</p>')


def heyhey_stream():
    from random import randrange
    resp = urllib2.urlopen(url + 'stream/?token=' + token)
    resp_json = json.loads(resp.read())
    count = len(resp_json['results'])
    today_girl = resp_json['results'][randrange(count)]
    img = '<img src="{url}" />'.format(url=today_girl['image'])
    return HTML(img)


def heyhey_today():
    resp = urllib2.urlopen(url + 'girl_of_the_day/?token=' + token)
    resp_json = json.loads(resp.read())
    today_girl = resp_json['results'][0]
    img = '<img src="{url}" />'.format(url=today_girl['image'])
    return HTML(img)


def heyhey_today_more():
    import datetime
    today = datetime.date.today().strftime('%Y-%m-%d')
    resp = urllib2.urlopen(
        url + 'girl_of_the_day/' + today + '/?token=' + token
    )
    resp_json = json.loads(resp.read())
    imgs = []
    for data in resp_json:
        imgs.append('<img src="{url}" />'.format(url=data['image']))
    return HTML(''.join(imgs))


def load_ipython_extension(ipython):
    # The ``ipython`` argument is the currently active
    # :class:`InteractiveShell` instance that can be used in any way.
    # This allows you do to things like register new magics, plugins or
    # aliases.
    ip = get_ipython()

    def heyhey(self, string):
        if token == '':
            return HTML('<p>Please set your API token first</p>')
        args = string.split()
        if len(args) == 0:
            return heyhey_stream()
        elif args[0] == 'today':
            if len(args) == 1:
                return heyhey_today()
            elif len(args) == 2 and args[1] == 'more':
                return heyhey_today_more()
            else:
                return warn_html
        else:
            return warn_html

    ip.define_magic('heyhey', heyhey)
    print('Register heyhey extension')


def unload_ipython_extension(ipython):
    # If you want your extension to be unloadable, put that logic here.
    pass
