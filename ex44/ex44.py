class Parent(object):

    def override(self):
        print("PARENT override()")

    def implict(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

dad.implict()
print("---------")
son.implict()
print()

dad.override()
print("---------")
son.override()
print()

dad.altered()
print("---------")
son.altered()
print()