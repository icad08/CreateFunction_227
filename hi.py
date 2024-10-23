def convert_temp(value, unit): 
    
    if unit == 'c' or unit == 'C':
        # konversi Celcius ke Fahrenheit
        converted_temp = (value * 9/5) + 32
        return converted_temp, 'F'
    elif unit == 'f' or unit == 'F':
        # konversi Fahrenheit ke Celsius
        converted_temp = (value - 32) * 5/9
        return converted_temp, 'C'
    else:
        return "Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit."

# masukin inputntya
value = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C or F): ")

# manggil nilai yg ada di fungsi dimasukin ke variabel result
result = convert_temp(value, unit)
print(result)