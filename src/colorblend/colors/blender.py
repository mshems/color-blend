from functools import reduce
from color import Color


def product(items):
    return reduce(lambda x, y: x*y, items)


def blend(ratios):
    if type(ratios) is list:
        ratios = {color: 1 for color in ratios}
    total = float(sum(ratios.values()))
    rho = product([color.rho**(weight/total) for color, weight in ratios.items()])
    return Color.from_reflectance(rho)


def spectrum_blend(color_a, color_b, steps):
    spectrum = [color_a]
    for i in range(0, steps):
        spectrum.append(blend({color_a: steps-i, color_b: 1+i}))
    spectrum.append(color_b)
    return spectrum
