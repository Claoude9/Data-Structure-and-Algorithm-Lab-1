n = int(input("Enter the number of rows: "))

if n % 2 == 0:
    print("\nPlease provide an odd number.")
else:
    for i in range(1, n + 1, 2):  
        spaces = (n - i) // 2      
        print(' ' * spaces + '*' * i)

    for i in range(n - 2, 0, -2):  
        spaces = (n - i) // 2     
        print(' ' * spaces + '*' * i)
    