class Mandelbrot:

    def __init__(self, max_iteration):
        self.max_iterations = max_iteration

    def getIterations(self, a, b):
        z = complex(0, 0)
        c = complex(a, b)

        iterations = 0

        while iterations < self.max_iterations:
            z = z*z + c

            if abs(z) > 4:
                break

            iterations += 1

        return iterations
