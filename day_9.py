print("--- Square pattern ---")
for i in range(10):
    for j in range(10):
        print("*", end="")
    print()
print("\n--- Right triangle pattern ---")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
print("\n--- Inverted right triangle pattern ---")
for i in range(5, 0, -1):
    for j in range (i):
        print("*", end="")
    print()









    print("--- multiplication table ---")
    try:
        size = int(input("Enter the size of the multiplication table (e.g., 5 or 10): "))
        for i in range (1, size + 1):
            for j in range (1, size + 1):
                product = i * j
                print(f"{product}\t", end="")
            print()
    except ValueError:
        print("Invalid input. Please enter a valid integer for the size of the multiplication table.")