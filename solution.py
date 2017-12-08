class FileReader:

    def __init__(self, way):
        self.way = way

    def read(self):
        try:
            with open(self.way, 'r') as f:
                data = str(f.read())
                return data
        except IOError:
            string = ""
            return string
