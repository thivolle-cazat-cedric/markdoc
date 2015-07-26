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
SECRET_KEY = ''

START_URI = ''

# translate language
FULL_LANGUAGES = {
	'fr' : {
		'fr' : 'Français',
		'en' : 'Anglais',
		'es' : 'Espagnole',
		'cn' : 'Chinoi',
		# ...
	},
	'en' : {
		'fr' : 'French',
		'en' : 'English',
		'es' : 'Spanish',
		'cn' : 'chinese',
		# ...
	},
	'es' : {
		'fr' : 'Francés',
		'en' : 'Inglés',
		'es' : 'Español',
		'cn' : 'Chino',
		# ...
	}
}

NAV_ITEMS = []

#
##############
# DOC CONFIG #
##############
#


# name of project
PROJECT_NAME = "Project name"

# Descripyion of Project
PROJECT_DESCRITION = """
documentation of project [...]
"""

# version of project
PROJECT_VERSION = "0.0.1-b"

# version of author
PROJECT_AUTHOR = "THIVOLLE-CAZAT Cédric"

# some solution to contact you, mail, contact url, ...
PROJECT_CONTACT = "mail@exemple.com"

# REPOSITORIE OF PROJECT
PROJECT_REPOSITORIE = "https://github.com/<login>/<PROJECT_NAME>"

# prefix in title header html 
PREF_TITLE = "@doc "

# set default language
DEFAULT_LANG = 'fr'

# extend of marckdown file (md|MD) are recomanded
EXTEN_MD = 'md'

# allowd language in documentation
LANGUAGES = ['fr', 'en']

# path start of doc marckodown from www-askcli dir
# Finish by '/'
# specipy the full path
PATH_DIR_DOC ='/var/doc/'