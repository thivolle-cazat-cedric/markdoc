# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
from jinja2 import Markup, escape
from flask import current_app
from re import sub

def render_breadcrumb(items):
    
    START_URI = current_app.jinja_env.globals['START_URI']

    breadcrumb = '<ol class="breadcrumb">'
    breadcrumb += '<li><a href="{0}"><i class="fa fa-home"></i></a></li>'.format(START_URI)

    i = 0
    for item in items:
        uri = sub('\/+', '/', '{0}/{1}/'.format(START_URI,'/'.join(items[0:i])))

        if i == len(items)-1:
            breadcrumb += '<li class="active">{0}</a></li>'.format(item)
        else:
            breadcrumb += '<li><a href="{0}">{1}</a></li>'.format(uri,item)
        
        i += 1
    
    breadcrumb += '</ol>'

    return Markup(breadcrumb)