print("What do you want to calculate? \n-Voltage\n-Current\n-Resistance")
print()
choice = input()

if choice == "Voltage":
    Current = float(input("\nEnter the value for current: "))
    Resistance = float(input("Enter the value for resistance: "))
    Voltage = Current * Resistance
    print(f"\nAnswer: {Voltage:.2f} V")
    
elif choice == "Current":
    Voltage = float(input("\nEnter the value for voltage: "))
    Resistance = float(input("Enter the value for resistance: ")) 
    
    if Resistance == 0:
        print("Error: Resistance cannot be zero.")
    else:
        Current = Voltage / Resistance
        print(f"\nAnswer: {Current:.2f} A")
        
elif choice == "Resistance":
    Voltage = float(input("\nEnter the value for voltage: "))
    Current = float(input("Enter the value for current: "))
    
    if Current == 0:
        print("Error: Current cannot be zero.")
    else:
        Resistance = Voltage / Current
        print(f"\nAnswer: {Resistance:.2f} ohms")
        
else:
    print("Please input valid value.")
    