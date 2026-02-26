my_money = 1000
car_price = 1000
can_afford = my_money >= car_price
is_exact_price = my_money == car_price
print("can_i_buy_car?")
print(can_afford)
print("is_it_exact_price?")
print(is_exact_price)
has_license = True
can_legally_drive = (has_license and can_afford)
print("can i buy AND drive this car")
print(can_legally_drive)