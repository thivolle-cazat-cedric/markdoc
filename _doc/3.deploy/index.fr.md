# Mise en production

--- 

Le module Flask est compatible apache2 et nginx. Je vous parlerais de la mise en production de apache2 dans un premier temps.

Il est recommandé de ne pas utilisé de variables de d'environnement pour la mise en production du site. Modifier le fichier *app/config/env/prod.py*


### [Apache config](./1.Apache)