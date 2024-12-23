class Cons:
    def __init__(self):
        self.greet = "Good Mng"

    def display(self):
        print("Msg =", self.greet)

    def __del__(self):
        print("object destroyed")

o = Cons()
o.display()
print(o)
del o

OUTPUT:
       Msg = Good Mng
       <__main__.Cons object at 0x780175172e50>
       object destroyed
