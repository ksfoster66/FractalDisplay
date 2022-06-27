import Zoom


class ZoomList(object):
    center_x = 0
    center_y = 0
    scale = 1
    zooms = []

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def add(self, zoom):
        self.zooms.append(zoom)

        self.center_x += (zoom.x - self.width/2)*self.scale
        self.center_y += (zoom.y - self.height/2)*self.scale

        self.scale *= zoom.scale

    def do_zoom(self, x, y):
        xFrac = (x-self.width/2)*self.scale + self.center_x
        yFrac = (y - self.height/2)*self.scale + self.center_y

        return xFrac, yFrac

    def scroll(self, x, y):
        self.center_x += x*self.scale
        self.center_y += y*self.scale
