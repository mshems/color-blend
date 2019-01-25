import reflectance


class Color(object):
    def __init__(self, rgb, rho):
        self.rgb = rgb
        self.rho = rho

    def __hash__(self):
        return hash(repr(self))

    def __repr__(self):
        return '#{0:02x}{1:02x}{2:02x}'.format(self.rgb[0], self.rgb[1], self.rgb[2])

    @classmethod
    def from_reflectance(cls, rho):
        return Color(reflectance.to_rgb(rho), rho)

    @classmethod
    def from_rgb(cls, rgb):
        return Color(rgb, reflectance.calculate(rgb))