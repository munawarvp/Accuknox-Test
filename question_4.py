'''
Topic: Custom Classes in Python
Description: You are tasked with creating a Rectangle class with the following requirements:

1. An instance of the Rectangle class requires length:int and width:int to be initialized.
2. We can iterate over an instance of the Rectangle class 
3. When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}
'''

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Yield length and width in the specified dictionary format
        yield {'length': self.length}
        yield {'width': self.width}

# Testing the Rectangle class
rectangle = Rectangle(9, 10)

# Iterating over the instance
for attribute in rectangle:
    print(attribute)


'''
Output:
{'length': 9}
{'width': 10}

The __iter__ method will yield the length and width in the specified dictionary format for an instance of the Rectangle class.

'''