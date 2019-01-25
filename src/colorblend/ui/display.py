from graphics import *
from colorblend.colors.color import Color
from colorblend.colors.blender import blend, spectrum_blend
from colorblend.colors.words import ColorWord
import matplotlib.pyplot as plt


def draw_swatches(colors):
    swatches = len(colors)

    win_width = max(100, 50*swatches)
    swatch_width = win_width / swatches
    win_height = swatch_height = swatch_width

    win = GraphWin('window', win_width, win_height)

    for i in range(0, swatches):
        r = Rectangle(Point(i * swatch_width, 0), Point(swatch_width + i * swatch_width, swatch_height))
        r.setFill(color=color_rgb(*colors[i].rgb))
        r.draw(win)
    win.getMouse()


def main():
    a = Color.from_rgb([130,26, 34])
    b = Color.from_rgb([229,192,82])
    result = blend({a:1, b:1})

    plt.plot(a.rho, color_rgb(*a.rgb))
    plt.plot(b.rho, color_rgb(*b.rgb))
    plt.plot(result.rho, color_rgb(*result.rgb))
    # plt.show()

    c1 = ColorWord.create('b')
    c2 = ColorWord.create('brrr')
    c3 = c1 + 'rrr'

    # draw_swatches([a, result, b])
    draw_swatches(spectrum_blend(a, b, 8))
    # draw_swatches([c1.color, c2.color, c3.color])


if __name__ == '__main__':
    main()