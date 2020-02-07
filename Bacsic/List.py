my_list = [1024, 3, True, 6.5]
my_list.append(False)
print(my_list)

my_list.insert(4,4.5)
print(my_list)
print(my_list.pop())
print(my_list)
print(my_list.pop(1))
print(my_list)
my_list.pop(2)
print(my_list)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
print(my_list.count(4.5))
print(my_list.index(4.5))
del my_list[2]
print(my_list)

print(list(range(5, 12, 2)))