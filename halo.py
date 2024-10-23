import math

# Lambda function to calculate the area of a circle
area_of_circle = lambda r: math.pi * r**2

# Input dari pengguna untuk radius
radius = float(input("Masukkan jari-jari lingkaran: "))  # Mengonversi input ke float
area = area_of_circle(radius)

print(f"Luas lingkaran dengan jari-jari {radius} adalah {area:.2f}")