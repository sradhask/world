def convert_temperature(value, unit_from, unit_to):
    if unit_from == 'Celsius' and unit_to == 'Fahrenheit':
        return (value * 9/5) + 32
    elif unit_from == 'Fahrenheit' and unit_to == 'Celsius':
        return (value - 32) * 5/9
    else:
        return "Conversion not supported"

def main():
    value = float(input("Enter the temperature value: "))
    unit_from = input("Convert from (Celsius/Fahrenheit): ").capitalize()
    unit_to = input("Convert to (Celsius/Fahrenheit): ").capitalize()
    
    result = convert_temperature(value, unit_from, unit_to)
    if isinstance(result, str):
        print(result)
    else:
        print(f"{value}°{unit_from[0]} is {result}°{unit_to[0]}")

if __name__ == "__main__":
    main()
