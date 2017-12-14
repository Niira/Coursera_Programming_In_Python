import os
import tempfile


class File:
    def __init__(self, path):
        self.path = path

    def write(self, data):
        with open(self.path, 'a') as f:
            f.write(data)

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def __str__(self):
        return self.path

    def __add__(self, second):
        dir_new = tempfile.gettempdir()
        path_new = os.path.join(dir_new, 'new_file.txt')
        newfile = File(path_new)
        with open(newfile.path, 'a') as f:
            f.write(self.read())
        with open(newfile.path, 'a') as f:
            f.write(second.read())
        return newfile

    def __iter__(self):
        self.line = open(self.path, 'r')
        return self.line

    def next(self):
        line = self.line.readline()
        if line != '':
            return line
        raise StopIteration


# file1 = File('/home/nyarina/PycharmProjects/untitled3/file.txt')
# file2 = File('/home/nyarina/PycharmProjects/untitled3/file1.txt')
# new_file = file1 + file2
# new_file.write('arina')
# file1.write('arina')
# file1.write('arina1')
# print(file1.read())
