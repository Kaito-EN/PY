stock = ["hero", "my lover", "my everthing"]
try:
    new_couunt = int(input("enter the number of items you adding:"))
    for i in range(new_couunt):
        new_items = input ("enter the name of new love: ")
        stock.append(new_items)
except ValueError:
    print("that was not a numer ")
print("your stuck is:", stock)
print(len(stock))