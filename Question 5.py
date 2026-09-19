from abc import ABC, abstractmethod


class FileHandler(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class TextFileHandler(FileHandler):

    def read(self):
        print("Reading data from a text file.")

    def write(self, data):
        print("Writing to text file:", data)


class BinaryFileHandler(FileHandler):

    def read(self):
        print("Reading data from a binary file.")

    def write(self, data):
        print("Writing to binary file:", data)


# Create objects
text_handler = TextFileHandler()
binary_handler = BinaryFileHandler()

# Use the methods
text_handler.read()
text_handler.write("Hello World")

binary_handler.read()
binary_handler.write(b"Binary Data")

