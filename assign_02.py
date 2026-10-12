#!/usr/bin/env python3
# Created By: Alex OBrien
# Date: Oct 11, 2026
# This program asks the user for measurements of a
# triangular prism and then calculates
# the surface area and volume.

# Prompt the user for the triangular base dimensions
b = float(input("Enter the base of the triangle (b): "))
h = float(input("Enter the height of the triangle (h): "))

# Prompt the user for all three side lengths of the triangle
s1 = float(input("Enter side 1 length of the triangle: "))
s2 = float(input("Enter side 2 length of the triangle: "))
s3 = float(input("Enter side 3 length of the triangle: "))

# Prompt the user for the length of the prism
L = float(input("Enter the length of the prism (L): "))

# Calculate the volume & SA
base_area = 0.5 * b * h
volume = base_area * L
surface_area = b * h + (s1 + s2 + s3) * L

# Show the results to user
print("\n--- Results ---")
print(f"Volume: {volume:.2f} cubic units")
print(f"Surface Area: {surface_area:.2f} square units")