#-*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
from flask import render_template, Blueprint, current_app, request, abort, g, session
from flask import Markup
from mistune import markdown
from app.utils.errors import render_error, is_err_language

from app.utils.docker import MarkDocker

SITE = Blueprint('site', __name__)

INDEX_PAGE = ['', 'index.html', 'home', 'home/']


@SITE.url_defaults
def add_ref_formule(endpoint, values):
    values.setdefault('lang', g.lang)

@SITE.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang = values.pop('lang')
    current_app.jinja_env.globals['LANG'] = g.lang


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


    doc = MarkDocker(
        base_dir=current_app.config['PATH_DIR_DOC'],
        language=g.lang,
        path_file=path,
        EXTEN_MD=current_app.config['EXTEN_MD']
    )

    current_app.jinja_env.globals['CURENT_DOC_FILE'] = doc


    if not doc.exist():
        if is_err_language(doc):
            body = render_error(404, g.lang, path=path)
            return render_template('err/index.html', body=body), 404
        else:
            abort(404)

    return render_template('doc.html', path=path)

