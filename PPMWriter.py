class PPMWriter(object):

    def __init__(self, filename, width, height):
        self.filename = filename

        with open(filename, "w") as output_file:
            print("P3", file=output_file)
            print(str(width) + " " + str(height), file=output_file)
            print(255, file=output_file)

    def write_to_file(self, content):
        with open(self.filename, "a") as output_file:
            print(content, file=output_file)
