from os.path import basename, dirname, exists, isfile
from mistune import Markdown, Renderer


class html_docker(object):
    """
    @todo document me 
    docstring for html_docker
    """

    _EXTEN_MD='md'
    _path = ''
    _file_name = ''
    base_dir = ''
    language = ''
    

    def __init__(self, base_dir, language, path_file='index.md', EXTEN_MD='md'):
        """
        :param str base_dir: the dir root of markdown doc
        :param str path_file: path to file
        :param str EXTEN_MD: exten if markdown files
        """

        self.set_base_dir(base_dir)
        self.language = language
        self._EXTEN_MD = EXTEN_MD
        self.set_path_file(path_file)


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

        self._path = "{0}{2}".format(self.base_dir,self.language, path)

        self._file_name = basename(path_file)

        if '.' in self._file_name:
            explose = self._file_name.split('.')
            exten = explose.pop(-1)

            if exten != self._EXTEN_MD:
                self._file_name += '.{0}.{1}'.format(self.language, self._EXTEN_MD)

            else:
                self._file_name = ''.join(explose)+'.{0}.{1}'.format(self.language, self._EXTEN_MD)


        else: 
            self._file_name += '.{0}.{1}'.format(self.language, self._EXTEN_MD)

        print(self.language)

    def get_full_name(self):
        """
        :rtype: str
        :return: le nom complet du fichier
        """

        return "{0}/{1}".format(self._path, self._file_name)

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
