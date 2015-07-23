#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

"""Ce module contient la function d'initilisation de l'application"""

from flask import Flask

from app.config.loader import config_loader


DB = SQLAlchemy()

def create_app(env='prod', module="all"):
    """
    Initialise l'application (configuration, blueprints, base de données, ...)

    :param str env: le nom de l'environement (dev, prod, tests, ...)

    :return: l'application initilisée
    :rtype: flask.Flask
    """
    
    app = Flask('doc-askcli', template_folder="app/templates", static_folder="app/lib")

    config_loader(app.config, env)



    @app.errorhandler(404)
    def err_too_many_requests(e):
        return 'err 404'
