class RGB(object):

    def __init__(self, r=0, g=0, b=0):
        self.r = r
        self.b = b
        self.g = g

    def __sub__(self, other):
        result = RGB()
        result.r = self.r - other.r
        result.g = self.g - other.g
        result.b = self.b - other.b

        return result
