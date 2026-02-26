name = input("enter your name pls: ")
age = int(input("enter your age: "))
experience = int(input("years of experience: "))
is_allowed = (age >= 18 and experience >= 2)
print ("can enter:", is_allowed)
appel = input("write the word 'appel' to continue: ")
appel = appel.replace("appel", "i miss rasima")
print(appel)
print(len(appel.split()))
print(len(name))
print(name.upper())






