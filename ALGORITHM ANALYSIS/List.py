def test1():
    list =[]
    for i in range(1000):
        list = list + [i]
    return list

def test2():
    list =[]
    for i in range(1000):
        list.append(i)
    return list

def test3():
    list =[i for i in range(1000) ]
    return list

def test4():
    l = list(range(1000))
    return l
print(test4())