import Mandelbrot
from RGB import RGB
from ZoomList import ZoomList
from Zoom import Zoom
from Mandelbrot import Mandelbrot


class FractalCreator(object):

    def __init__(self, width, height, num_of_iterations):
        self.width = width
        self.height = height
        self.fractal = [[0 for y in range(self.height)] for x in range(self.width)]
        self.histogram = [0] * num_of_iterations
        self.ranges = []
        self.range_totals = []
        self.colors = []
        self.zoomlist = ZoomList(width=width, height=height)
        self.got_starting_range = False
        self.max_iterations = num_of_iterations
        self.mandelbrot = Mandelbrot(num_of_iterations)

    def run(self):
        self.calculate_iterations()
        self.calculate_ranges()
        self.draw_fractal()

    def add_zoom(self, x, y, scale):
        self.zoomlist.add(Zoom(x, self.height - y, scale))

    def add_scroll(self, x, y):
        self.zoomlist.scroll(x, y)

    def add_range(self, range_end, r, g, b):
        self.ranges.append(range_end * self.max_iterations)
        self.colors.append(RGB(r, g, b))

        if self.got_starting_range:
            self.range_totals.append(0)
        else:
            self.got_starting_range = True

    def get_range(self, iteration):
        range_i = 0

        for i in range(1, len(self.ranges)):
            range_i = 1
            if self.ranges[i] > iteration:
                break

        range_i = range_i - 1
        return range_i

    def calculate_iterations(self):
        print("Calculating iterations")
        # Calculating the iterations
        for y in range(self.height):
            for x in range(self.width):

                coords = self.zoomlist.do_zoom(x=x, y=y)
                iterations = self.mandelbrot.getIterations(coords[0], coords[1])

                self.fractal[x][y] = iterations

                if iterations != self.max_iterations:
                    self.histogram[iterations] += 1

    def calculate_ranges(self):
        print("Calculating ranges")
        # Calculating the ranges
        rangeindex = 0
        for i in range(self.max_iterations):
            pixels = self.histogram[i]

            if i >= self.ranges[rangeindex + 1]:
                rangeindex += 1

            self.range_totals[rangeindex] += + pixels

    def draw_fractal(self):
        print("Drawing fractal")
        # Create the file writer
        filename = "example.ppm"
        with open(filename, "w") as output_file:
            print("P3", file=output_file)
            print(str(self.width) + " " + str(self.height), file=output_file)
            print(255, file=output_file)

            # Draw the fractal
            total = 0
            for i in range(self.max_iterations):
                total = total + self.histogram[i]

            for y in range(self.height):
                for x in range(self.width):
                    iteration = self.fractal[x][y]
                    iteration_range = self.get_range(iteration)
                    range_total = self.range_totals[iteration_range]
                    range_start = self.ranges[iteration_range]

                    start_color = self.colors[iteration_range]
                    end_color = self.colors[iteration_range + 1]
                    diff_color = end_color - start_color
                    red = 0
                    green = 0
                    blue = 0

                    if iteration != self.max_iterations:

                        total_pixels = 0
                        for i in range(range_start, iteration):
                            total_pixels += self.histogram[i]

                        red = int(start_color.r + pow(diff_color.r, total_pixels/range_total))
                        blue = int(start_color.b + pow(diff_color.b, total_pixels/range_total))
                        green = int(start_color.g + pow(diff_color.g, total_pixels/range_total))

                    print("Writing pixel " + str(x) + ", " + str(y))
                    # Write to file here
                    print(str(red) + " " + str(green) + " " + str(blue) + " ", file=output_file)
