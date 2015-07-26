# ![Image of Yaktocat](http://doc.thivolle-cazat.fr/public/markdoc/logo-50.png)  MarkDoc 
---

I'm sorry for my bad english

MarkDoc is a tool that allows you to generate a web site of code documentation according to marckdown files. The module lets you manage documentation multi language, a folder tree and automatic materals menu.

## How to structured the documentation files ?

Not realy hard, MarkDoc is friendly, *we talke about config later (:D)*. Simply to know write in markdown. This module are nice, because it use the same syntax like [gitlab](http://doc.gitlab.com/ce/markdown/markdown.html) and [github](https://help.github.com/articles/markdown-basics/). You can simply have a documentation on your git repositories, and you can propose this documentation on a personnal website easily.

#### naming of files and directories

The files look like this : 
```
<index>.<nomfichier><lang>.md
 -----   ----------  ----
   |      |            |_________ lang of content in files
   |      |______________________ name of files, and is the name in lateral menu. the name of sections
   |_____________________________ order of files in laterale menu
```

Les dossier eux sont nomé simplement sans extension <lanf>.md
Les fichiers sont nomé de la sorte : 
```
<index>.<nomdossier>
  ---------- 
   |______________________ name of directory, and is the name in lateral menu. the name of sections
```

``/!\ Warning every directory must have file named index.<lang>.md``

#### Tree 

*exemple :*
```
 + doc_dir 
    | - index.fr.md
    | - index.en.md
    | - installation.fr.md
    | - installation.en.md
    | - configuration.fr.md
    | - configuration.en.md
    | + deploy
    |   | - index.fr.md
    |   | + apache/
    |   |   | - index.fr.md
    |   |   | - index.en.md
    |   | + nginx/
    |   |   |   | - index.fr.md
    |   |   |   | - index.en.md
	| - _ignore_file.md
	| - .ignore_file2.md
	[...]
```

This is easy you see? look the render

<img src="http://doc.thivolle-cazat.fr/public/markdoc/preview.png" class="img-responsive img-thumbnail">


