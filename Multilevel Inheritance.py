class Parent():
    def fun1(self):
        print("first function")
class Child(Parent):
    def fun2(self):
        print("second function")
class Child2(Child):
    def fun3(self):
        print("third function")
ob = Child2()
ob.fun1()
ob.fun2()
ob.fun3()

OUTPUT:
       first function
       second function
       third function



      
