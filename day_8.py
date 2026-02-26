animals = ["dog", "cat", "mouse", "hamster"]
print(f"Original list: {animals}")

try:
    index = int(input(" enter the number of the animals you want to add to the index:"))
    for i in range(index):
        new_animal = input("Enter the name of the animal you want to add:")
        animals.append(new_animal)

    died = input("do you want to remove an animal? (yes/no): ")
    if died.lower() == "yes":
        remove_amimal = input("what is the animal you want to remove:")
        if remove_amimal in animals:
            animals.remove(remove_amimal)
            print(f"successfully removed {remove_amimal}!")
        else:
            print(f"{remove_amimal} is not in the list.")
except ValueError:
    print("that was not a number ")
print(f"final list is: {animals}")

  