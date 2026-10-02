# give the list to choose what we convert into fahrenheit,celsius,kelvin

from unittest import case


temperature_list=["fahrenheit", "celsius", "kelvin"]
select=input("Select the temperature unit to convert (fahrenheit, celsius, kelvin): ").lower()

if select in temperature_list:
    print(f"You selected {select}.")
else:
    print("Invalid selection.")

match select:
    case "fahrenheit":
        celsius=float(input("Enter temperature in Celsius: "))
        fahrenheit=(celsius*9/5)+32
        print(f"{celsius}°C is equal to {fahrenheit}°F.")
    case "celsius":
        fahrenheit=float(input("Enter temperature in Fahrenheit: "))
        celsius=(fahrenheit-32)*5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C.")
    case "kelvin":
        celsius=float(input("Enter temperature in Celsius: "))
        kelvin=celsius+273.15
        print(f"{celsius}°C is equal to {kelvin} K.")
