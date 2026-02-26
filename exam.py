name = input("pleaase enter your name: ")
budget = int(input("enter your budget: "))
car_price = 5000
can_buy = budget >= car_price and len(name) > 3
print("can buy?")
print(can_buy)
review = input("write a review (use the word 'bad'):")
review = review.replace("bad","great")
print("fixed review: " + review)
print("print words in review:", len(review.split()))
print("costumer name:", name.upper())
