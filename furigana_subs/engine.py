from tempfile import NamedTemporaryFile
import regex as re

from .parser import Parser


class SubtitleEngine(object):
    def __init__(self, filename, tmp_path='/tmp'):
        self.input_filename = filename
        self.output_file = NamedTemporaryFile(dir=tmp_path, delete=False)

    def add_furigana(self):
        '''
        We go through every line of the subtitle file and parse it only if
        we find kanji in it. We then return the resulting file handler.
        '''
        p = Parser()

        with open(self.input_filename, 'r') as f:
            with open(self.output_file.name, 'w') as o:
                for l in f:
                    res = re.findall(r'\p{Han}', l)

                    if len(res) > 0:
                        new_line = p.parse_sentence(l)
                        o.write(new_line)
                    else:
                        o.write(l)

        return self.output_file.file
