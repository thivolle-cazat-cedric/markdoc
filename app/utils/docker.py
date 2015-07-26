# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
from os import listdir
from os.path import basename, dirname, exists, isfile
from mistune import Markdown, Renderer
from re import sub

class FilesDoc(object):
    """
    simplement un objet ficiers 
    """

    basename = ""
    file_name = "",
    is_file = True,
    is_current = True

    def __init__(self, basename, file_name, is_file=True, is_current=False):
        """
        :param str basename: path of file
        :param str file_name: name of file
        :param bool is_file: if is file is True, if is directory is False
        """
        self.set_basename(basename)
        self.file_name = file_name
        self.is_file = is_file
        self.is_current = is_current

    def __str__(self):
        return self.full_name()

    def __repr__(self):
        return "<FilesDoc : {0}>".format(self.full_name())

    def set_basename(self, basename):
        """
        :param str basename: path of file

        permet de seter la valeur basename
        """

        self.basename = sub('\/+', '/', basename)
        if self.basename and self.basename[-1] == '/':
            self.basename = self.basename[:-1]

    def full_name(self):
        """
        :rtype: str
        :return: the file path and filename in systeme
        """

        return "{0}/{1}".format(self.basename, self.file_name)

    def get_human_name(self):
        return self.file_name.replace('.', ' ', 1)


class MarkDocker(object):
    """
    @todo document me 
    docstring for html_docker
    """

    _EXTEN_MD='md'
    _path = ''
    _file_name = ''
    base_dir = ''
    language = ''
    

    def __init__(self, base_dir, language, path_file='index', EXTEN_MD='md'):
        """
        :param str base_dir: the dir root of markdown doc
        :param str path_file: path to file
        :param str EXTEN_MD: exten if markdown files
        """

        self.set_base_dir(base_dir)
        self.language = language
        self._EXTEN_MD = EXTEN_MD
        self.set_path_file(path_file)

    def __repr__(self):
        return "<html_docker : {0}>".format(self.get_full_name())

    def __str__(self):
        return "file : {0}>".format(self.get_full_name())

    def set_base_dir(self, base_dir):
        """
        :param str base_dir: path of base dire
        """

        if len(base_dir) > 0 and base_dir[-1] != '/':
            base_dir += '/'

        self.base_dir = base_dir


    def set_path_file(self, path_file):
        """
        :param str path_file: path to file
        """
        path = dirname(path_file)

        self._path = "{2}".format(self.base_dir,self.language, path)

        self._file_name = basename(path_file)
        if len(self._file_name) < 1:
            self._file_name='index'

        if '.' in self._file_name:
            explose = self._file_name.split('.')
            exten = explose.pop(-1)

            if exten != self._EXTEN_MD:
                self._file_name += '.{0}.{1}'.format(self.language, self._EXTEN_MD)

            else:
                self._file_name = ''.join(explose)+'.{0}.{1}'.format(self.language, self._EXTEN_MD)


        else: 
            self._file_name += '.{0}.{1}'.format(self.language, self._EXTEN_MD)


    def get_full_name(self):
        """
        :rtype: str
        :return: le nom complet du fichier
        """

        return "{0}{1}/{2}".format(self.base_dir, self._path, self._file_name)

    def get_human_name(self):
        """
        :rtype: str
        :return: le nom du fichier sans extension ni information sur la langue
        """

        explose = self._file_name.split('.')

        if len(explose)>2:
            return '.'.join(explose[:-2])

        else:
            return self._file_name
        


    def exist(self):
        """
        :rtype: bool
        :return: si le fichier existe ou non
        """

        return (exists(self.get_full_name()) and isfile(self.get_full_name()))

    def get_content(self, escape=False, hard_wrap=True, use_xhtml=True, parse_block_html=True):
        """
        :rtype: mistune.Markdown
        :return: le contenu du fichier markdown

        :raise IOError: si le fichier n'exist pas.
        """

        if self.exist():
            markdown = Markdown(renderer=Renderer(
                escape=escape,
                hard_wrap=hard_wrap,
                use_xhtml=use_xhtml,
                parse_block_html=parse_block_html
            ))
            with open(self.get_full_name(), 'r') as f:
                m = markdown(f.read())
                f.close()

            return m 
            
        else:
            raise IOError

    def get_list_breadcrumb(self):
        """
        :rtype: list
        :return: le chemin du fichier sous forme de list
        """

        work = self.language + '/' + self._path + '/' +self._file_name.replace('.{0}'.format(self.language),'')
        work = sub('\/+', '/', work)

        if work and (work[0] == '.' or work[0] == '/') :
            work = work[1:]

        if work and (work[1] == '.' or work[1] == '/') :
            work = work[1:]

        return work.split('/')

    def get_brothers(self, char_ignor='_'):
        """
        :param str char_ignor: first charactere to ignore file

        :rtype: list of FilesDoc
        :return: les fichiers ce trouvant dans le meme dossier que le courant

        ignore the .<filename>
        """

        path="{0}{1}".format(self.base_dir, self._path)
        brothers = list()
        files = listdir(path)
        added = list()
        curent = '.'.join(self._file_name.split('.')[:-2])

        for f in files:

            if f and f[0] != char_ignor and f[0] != '.' and not(f[0] in char_ignor):

                f_explose = f.split('.')
                if len(f_explose) > 2:
                    doc_file = '.'.join(f_explose[:-2])
                else:
                    doc_file = f

                if not(doc_file in added) and f_explose[0] != 'index':

                    added.append(doc_file)
                    brothers.append(
                        FilesDoc(
                            self._path, 
                            doc_file, 
                            isfile("{0}/{1}".format(path, f)),
                            (doc_file == curent)
                        )

                    )

        return brothers

    def get_header_path(self):

        return self._path.split('/')[-1]


