my_set = {3,6,"cat",4.5,False}
print(len(my_set))
print(False in my_set)

your_set = {99,3,100}

#Returns a new set with all elements from both sets
print(my_set.union(your_set))
print(my_set | your_set)

#Returns a new set with only the elements common to both sets
print(my_set.intersection(your_set))
print(my_set & your_set)

#Returns a new set with all items from first set not in second
print(my_set.difference(your_set))
print(my_set - your_set)

#Asks whether all elements of one set are in the other
print({3,100}.issubset(your_set))
print({3,100} <= your_set )

my_set.add("Houses")
print(my_set)

my_set.remove(4.5)
print(my_set)

#Removes an arbitrary element from the set
my_set.pop()
print(my_set)

my_set.clear()
print(my_set)
