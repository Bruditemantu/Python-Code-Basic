# Ouestion No6
class Parent:
    def parent_method(self):
        print("This is a method from the Parent class")

class Child(Parent):  
    def child_method(self):
        print("This is a method from the Child class")

child = Child()
child.parent_method()  
child.child_method()
