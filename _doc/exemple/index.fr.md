# ![Image of Yaktocat](http://doc.thivolle-cazat.fr/public/markdoc/logo-50.png)  MarckDoc 
---

MarckDoc est un outil qui vous permet de générer un site internet de documentation de code en fonction de fichiers marckdown. Le module vous permet gèrer la documentation multi langage, une arborescences de dossier et des menu latérals automatique.

## Comment ce compose la structure de fichiers ?

Rien de compliquer, MarckDoc est assez simple *on parlera configuration et dépendances plus tard :D*. Il vous suffit de savoir écrire en Marckdown. Et ce module est gentil, car il utilise la même syntaxe que [gitlab](http://doc.gitlab.com/ce/markdown/markdown.html) et [github](https://help.github.com/articles/markdown-basics/). Vous pourrez facilement avoir une documentation sur votre repositories, mais vous pourrez aussi la porter sur un site perso sans trop de difficulté.

#### Nomination des fichiers et dossiers

Les fichiers sont nomé de la sorte : 
```
{{nomfichier}}{{lang}}.md
  ----------    ----
   |              |_______ langue dans le quelle est ecris le fichié
   |______________________ nom du fichier, qui sera également ajouter dans le menu latéral
```

Les dossier eux sont nomé simplement sans extension {{lanf}}.md
Les fichiers sont nomé de la sorte : 
```
{{nomdossier}}
  ---------- 
   |______________________ nom du dossier, qui sera également ajouter dans le menu latéral
```

``/!\ Attention chaque dossier doit contenir un index.{{lang}}.md``

#### Arborésence 

*exemple :*
```
 + doc_dir 
    | - index.fr.md
    | - index.en.md
    | - installation.fr.md
    | - installation.en.md
    | - configuration.fr.md
    | - configuration.en.md
    | + exemple
    |   | - index.fr.md
    |   | - config.fr.md
    |   | - run.fr.md
	| - _ignore_file.md
	| - .ignore_file2.md
	[...]
```

Ca à l'aire simple non ? mais c'es simple.


