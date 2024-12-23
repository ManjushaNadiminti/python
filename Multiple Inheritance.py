class ParentA:
    def fun1(self):
        print("first function")
class ParentB:
    def fun2(self):
        print("second function")
class Child(ParentA,ParentB):
    def fun3(self):
        print("third function")
ob = Child()
ob.fun1()
ob.fun2()
ob.fun3()

OUTPUT:
       first function
       second function
       third function
