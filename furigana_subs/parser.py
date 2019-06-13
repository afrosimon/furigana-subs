from natto import MeCab
import regex as re


class Word(object):
    '''
    Thin wrapper over a MeCab node, parsing the comma separated
    fields.
    '''
    def __init__(self, node):
        self.content = node.surface

        res = re.findall(r'\p{Han}', node.surface)

        if len(res) > 0:
            self.kanji = True
        else:
            self.kanji = False

        features = node.feature.split(',')

        # unreliable number of commas
        if len(features) > 7:
            self.furigana = features[7]
        else:
            self.furigana = None


class Parser(object):
    def __init__(self):
        self.mc = MeCab()

    def parse_sentence(self, line):
        '''
        We receive a line of japanese text, pass it through Mecab morphological
        analyzer and include furigana when needed (only for kanjis).
        '''
        new_line = ''

        for node in self.mc.parse(line, as_nodes=True):
            if not node.is_eos():
                word = Word(node)

                if word.kanji:
                    new_line += '{}[{}]'.format(word.content, word.furigana)
                else:
                    new_line += word.content

        return new_line
