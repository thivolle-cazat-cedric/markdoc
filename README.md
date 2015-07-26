# markdoc

---

un outil qui permet de gerner un site de documentation via des fichiers markdown

## Instatlation 

#### requirement

 * python2.7 ou +
 * virtualenv
 * pip


#### installation python 2.7

```
$ cd {{your-target-dir}}
$ git clone --recursive https://github.com/thivolle-cazat-cedric/markdoc.git
$ cd markdoc
$ mkdir env
$ virtualenv env/python2
$ source env/python2/bin/activate
$ pip install -r requirement.txt
$ cp app/config/default.py app/config/env/prod.py
$ ./markdoc.py runserver
```

