# Write a program to print the area of two rectangles having
# sides (4,5) and (5,8) respectively by creating a class named
#     'Rectangle' with a method named 'Area' which returns the area
# and length and breadth passed as parameters to its constructor.


class Rectangle:
    def __init__(self,atr_tuple):
        self.atr_tuple = atr_tuple

    def area(self):
        length =self.atr_tuple[0]
        breadth = self.atr_tuple[1]
        a = length*breadth
        return print(a)

rec1 = Rectangle((4,5))
rec2 = Rectangle((5,8))
rec1.area()
rec2.area()
