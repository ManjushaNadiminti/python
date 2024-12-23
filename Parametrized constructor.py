class Add:
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print(self.first)
        print(self.second)
        print(self.first + self.second)

a = Add(50, 60)
a.display()

OUTPUT: 
       50
       60
           110
