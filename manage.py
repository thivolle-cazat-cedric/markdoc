#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from flask import current_app
from flask.ext.script import Manager
from app.application import create_app

app = create_app()
manager = Manager(app)

@manager.command
def environement():
    "show the environement var"
    
    print(" Environement name : " + current_app.config['ENV_NAME'])
    if current_app.config['DEBUG']:
        from os import environ
        print(' Environement File:' + environ['ASKCLI_DOC_CONFIG'])


if __name__ == "__main__":
     manager.run()