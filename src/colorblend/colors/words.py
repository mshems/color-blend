from collections import Counter
from color import Color
from blender import blend

COLOR_MAP = {
    'r': Color.from_rgb([255,0,0]),
    'g': Color.from_rgb([0,255,0]),
    'b': Color.from_rgb([0,0,255]),
}


class ColorWord(object):
    def __init__(self, word, color):
        self.word = word
        self.color = color

    def __str__(self):
        return self.word

    def __len__(self):
        return len(self.word)

    def __add__(self, other):
        blend_ratio = {self.color: self.weight}
        if type(other) is ColorWord:
            new_word = self.word+other.word
            blend_ratio.update({other.color: other.weight})
        elif isinstance(other, basestring):
            new_word = self.word+other
            blend_ratio.update({color_of(other): weight_of(other)})
        else:
            raise TypeError()
        return ColorWord(new_word, blend(blend_ratio))

    @property
    def weight(self):
        return sum(1 for letter in self.word if letter in COLOR_MAP)

    @classmethod
    def create(cls, str):
        return ColorWord(str, color_of(str))


def weight_of(str):
    return sum(1 for letter in str if letter in COLOR_MAP)


def color_of(str):
    if len(str) == 1:
        return COLOR_MAP[str]
    else:
        return blend({COLOR_MAP[letter]: count for letter, count in Counter(str).items() if letter in COLOR_MAP})
