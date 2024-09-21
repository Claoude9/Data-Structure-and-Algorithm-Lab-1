temperature = float(input("Enter the temperature: "))
print("\nTypes of Conversion \nA- Fahrenheit to Celsius \nB- Celsius to Fahrenheit")
type = input("\nSelect conversion (type A/B): ")
type1 = type.upper()

if type1 == "A":
    Celsius = (temperature - 32) * 5/9
    print(f"\nAnswer: {temperature} Fahrenheit = {float(Celsius):.2f} Celsius")
elif type == "B":
    Fahrenheit = (9/5 * temperature) + 32
    print(f"\nAnswer: {temperature} Celsius= {float(Fahrenheit):.2f} Fahrenheit")
else:
    print ("Invalid Input")    
    