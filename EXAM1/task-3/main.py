# Function: Invert RGB Color
# Objective: Write a function `color_invert` that takes an RGB color tuple and returns the inverted color tuple.
# Parameters:
# - color: A tuple with three integers representing the RGB values of the color (each value ranges from 0 to 255).
# Returns:
# - A tuple representing the inverted RGB values.

def color_invert(color):
    r, g, b = color
    inverted_r = 255-r
    inverted_g = 255-g
    inverted_b = 255-b
    return (inverted_r, inverted_g, inverted_b)

color = (60, 120, 199)
inverted_color = color_invert(color)
print(inverted_color)