from FractalCreator import *

width = 1200
height = 800

num_of_iterations = 1000

fractal = FractalCreator(width=width, height=height, num_of_iterations=num_of_iterations)

# Add ranges
fractal.add_range(0, 0, 0, 0)  # Start Range
fractal.add_range(.1, 0, 255, 0)
fractal.add_range(1, 0, 0, 255)  # End Range

# Add Zooms and Scrolls
fractal.add_zoom(width/2, height/2, 4/width)
# fractal.add_scroll(-100, 0)

fractal.run()
