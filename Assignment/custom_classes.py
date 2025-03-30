# File: custom_classes.py

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {"length": self.length}
        yield {"width": self.width}

# Testing the iteration functionality
if __name__ == "__main__":
    rect = Rectangle(10, 5)
    for value in rect:
        print(value)
#Expected Output:

{'length': 10}
{'width': 5}
