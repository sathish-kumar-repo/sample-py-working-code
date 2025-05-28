import random as rdm

# prints a random value from the list
lst1 = [1, 2, 3, 4, 5, 6]
print(rdm.choice(lst1))


# Generates a random number between x to y
random_number = rdm.randint(1, 10)
print(random_number)


# Shuffle the List
mylist = ["apple", "banana", "cherry"]
rdm.shuffle(mylist)
print(mylist)


# Random number between 0 to 1
print(rdm.random())


