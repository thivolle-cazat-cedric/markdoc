#!/usr/bin/python
import sys, os
path_app = '/var/www/markdoc'
sys.path.insert(0, path_app)
os.chdir(path_app)

activate_this = '/var/www//markdoc/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from app.application import create_app
application = create_app()