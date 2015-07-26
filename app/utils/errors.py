#-*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
from mistune import Markdown, Renderer
from flask import render_template
from os import listdir
from os.path import basename, dirname, exists

def render_error(err_code, lang='en', path='', escape=False, hard_wrap=True, use_xhtml=True, parse_block_html=True):
    """
    :rtype: str
    :return: une page d'erreur markdown en html
    """

    try:
        content = render_template('err/{0}/{1}.md'.format(err_code, lang), path=path)
    except Exception, e:
        try:
            content = render_template('err/{0}/{1}.md'.format(err_code, 'en'), path=path)
        except Exception as e:
            raise e

    markdown = Markdown(renderer=Renderer(
        escape=escape,
        hard_wrap=hard_wrap,
        use_xhtml=use_xhtml,
        parse_block_html=parse_block_html
    ))
    
    return markdown(content)

def is_err_language(markdocker):
    

    if not exists(dirname(markdocker.get_full_name())):
        return False

    resp = False    
    file_name = basename(markdocker.get_full_name())
    file_explose = file_name.split('.')

    try:
        files = listdir(dirname(markdocker.get_full_name()))
    except Exception, e:
        return False

    if len(file_explose) < 3:
        return False
    else:
        target_file = '.'.join(file_explose[:-2])

    for f in files:
        explose = f.split('.')

        if len(file_explose) > 2:
            f_target = '.'.join(explose[:-2])

            if target_file == f_target:
                resp = True

    return resp

