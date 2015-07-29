# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

"""Ce module contient la function d'initilisation de l'application"""

from flask import Flask, redirect, render_template
from app.config.loader import config_loader
from app.utils import cusrom_jinja_filters 


def create_app(env='prod', module="all"):
    """
    Initialise l'application (configuration, blueprints, base de données, ...)

    :param str env: le nom de l'environement (dev, prod, tests, ...)

    :return: l'application initilisée
    :rtype: flask.Flask
    """
    
    from app.controllers.site import SITE
    app = Flask('doc-askcli', template_folder="app/templates", static_folder="app/lib")
    config_loader(app.config, env)

    app.jinja_env.filters['breadcrumb'] = cusrom_jinja_filters.render_breadcrumb

    for key in [
        'PROJECT_DESCRITION',
        'NAV_ITEMS',
        'FULL_LANGUAGES',
        'START_URI',
        'PROJECT_NAME',
        'LANGUAGES',
        'PREF_TITLE',
        'PROJECT_VERSION',
        'PROJECT_AUTHOR',
        'PROJECT_CONTACT',
        'PROJECT_REPOSITORIE',
        'ICON_IMG_LINK'
    ]:
        app.jinja_env.globals[key] = app.config[key]

    
    @app.route("/")
    def redirect_default():
        return redirect('/{0}/'.format(app.config['DEFAULT_LANG'])), 301

    app.register_blueprint(SITE, url_prefix='/<lang>/')


    @app.errorhandler(404)
    def err_too_many_requests(e):
        
        return render_template('err/404.html'), 404

    return app
