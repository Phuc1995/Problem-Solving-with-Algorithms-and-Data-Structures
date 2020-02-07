class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def show(self):
        return self.items

#Palindrome Checker
def pal_checker(a_string):
    char_deque = Deque()
    for ch in a_string:
        char_deque.addRear(ch)
    print(char_deque.show())
    result = True
    while char_deque.size() > 1 and result:
        firt = char_deque.removeFront() 
        print(firt)   
        last = char_deque.removeRear()
        print(last)
        if firt != last:
            result = False
    return result
print(pal_checker("ababa"))