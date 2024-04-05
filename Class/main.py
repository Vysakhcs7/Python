class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def display_details(self):
        print("Rectangle:")
        print("Width:",self.width)
        print("Height:",self.height)
        print(f"Area: {self.area()}cm²")
        print(f"Perimeter:{self.perimeter()}cm")


# Get input from the user for width and height
width = float(input("Enter the width of the rectangle in cm: "))
height = float(input("Enter the height of the rectangle in cm: "))

# Create an instance of the Rectangle class with user-provided values
oRectangle = Rectangle(width, height)

# Call the display_details method to display the rectangle's details
oRectangle.display_details()
########################################################################################################  