def convert_temperature(temp):
    try:
        value, unit = float(temp[:-1]), temp[-1].upper()  # Try to separate number & unit
    except ValueError:
        return "Invalid input! Please enter a number followed by C, F, or K."
    if unit == "C":
        f = (value*9/5)+32
        k = value + 273.15
        return f"{value}C = {f}F = {k}K"
    elif unit == "F":
        c = (value-32)*5/9
        k = value + 273.15
        return f"{value}F = {c}C = {k}K"
    elif unit == "K":
        c = value - 273.15
        f = (c * 9 / 5) + 32
        return f"{value}K = {f}F = {c}C"
    else:
        return "Invalid unit! Use C for Celsius, F for Fahrenheit, or K for Kelvin."

while True:
    user_input = input("Enter a temperature (e.g., 100C, 212F, 300K) or q to quit")
    if user_input.lower() == "q":
        print("Goodbye")
        break
    else:
        print(convert_temperature(user_input))
