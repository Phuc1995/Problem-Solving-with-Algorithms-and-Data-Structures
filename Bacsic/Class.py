class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    def show(self):
        print(self.num,"/", self.den)
    def __str__(self):
        return str(self.num) + '/' + str(self.den)
    def __add__(self, other_fraction):
        new_num = self.num*other_fraction.den + self.den*other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)
    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num

my_fraction = Fraction(3,5)
print(my_fraction)
my_fraction.show()

f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2 + f1
print(f3)

x = Fraction(1, 2)
y = Fraction(1, 2)
print(x + y)
print(x == y)