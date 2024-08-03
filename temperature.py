def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Define the boiling and freezing points of water in Celsius
boiling_point_celsius = 100
freezing_point_celsius = 0

# Convert to Fahrenheit
boiling_point_fahrenheit = celsius_to_fahrenheit(boiling_point_celsius)
freezing_point_fahrenheit = celsius_to_fahrenheit(freezing_point_celsius)

print(f"The boiling point of water in Fahrenheit is: {boiling_point_fahrenheit}°F")
print(f"The freezing point of water in Fahrenheit is: {freezing_point_fahrenheit}°F")
