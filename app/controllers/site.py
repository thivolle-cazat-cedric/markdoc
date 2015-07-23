# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
from flask import render_template, Blueprint, current_app, request, abort, g, session
from flask import Markup
from mistune import markdown

from app.utils.docker import html_docker

SITE = Blueprint('site', __name__)

INDEX_PAGE = ['', 'index.html', 'home', 'home/']


@SITE.url_defaults
def add_ref_formule(endpoint, values):
    values.setdefault('lang', g.lang)

@SITE.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang = values.pop('lang')

@SITE.before_request
def check_language():
    if not (g.lang in current_app.config['LANGUAGES']):
        if current_app.config['DEBUG']:
            return "<code>[DEBUG] : language not available. Check config['LANGUAGES']</code>"
        else:
            abort(404)

@SITE.route('', methods=['GET'])
@SITE.route('<path:path>', methods=['GET'])
def docker_page(path='index'):

    doc_file = html_docker(
        base_dir=current_app.config['PATH_DIR_DOC'],
        language=g.lang,
        path_file=path,
        EXTEN_MD=current_app.config['EXTEN_MD']
    )

    print(doc_file.get_full_name())

    if not doc_file.exist():
        abort(404)

    return doc_file.get_content()

