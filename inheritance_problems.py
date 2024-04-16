# Example 1

class A:
    def a(self):
        return "Funtion inside A"

class B:
    def a(self):
        return "Function inside B"

class C(B , A):
    pass

c = C()
print(c.a())
