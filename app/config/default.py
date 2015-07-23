# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

#
#########################
# DEFAULT CONFIGURATION #
#########################
#
# pleas don't touch ;-)

# nom de l'environement
ENV_NAME = "Default prod"

# afficher le debud flask et autre modul lie a flask
DEBUG = False

# clef de crypto pour les session
SECRET_KEY = '007'

# duree d une session
PERMANENT_SESSION_LIFETIME = (3600 * 24) * 7