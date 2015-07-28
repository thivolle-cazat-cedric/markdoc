# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

def config_loader(config, environment):
    """
    Charge la configuration de l'application.

    :param flask.Config config: généralement app.config
    :param str environement: le nom de l'environement (prod, dev, test, ...)

    :raises Exception: en cas d'erreur...
    :return: None

    L'ordre de chargement est le suivant :

      * la configuration par defaut (ami.config.default)
      * la configuration en fonction de l'environment (prod, dev, test, ...)
      * la configuration de l'utilisateur depuis le fichier definit dans la
        variable d'environement MARKCDOC_CONFIG.

    Il permet de surcharger la configuration.
    """

    config.from_object('app.config.default')
    try:
        config.from_object('app.config.env.%s' % (environment))
    except Exception as e:
        print(str("ERROR TO LOAD CONFIG ENVIRONEMENT : {0} [{1}]".format(environment, str(e))))
        
    
    try:
        config.from_envvar('MARKCDOC_CONFIG', silent=True)
    except Exception, e:
        print(str("ERROR TO LOAD CONFIG ENVIRONEMENT : {0} [{1}]".format(environment, str(e))))
