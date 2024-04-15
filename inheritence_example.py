 
 
 #simple inheritence
class A:
    pass
class B(A):
    pass

#multiple inheritence

class A:
    a = 1

class B:
    b = 2
class C(A,B):
    pass

c = C()
print(c.a , c.b)


#multilevel inheritance
class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
print(c.a)


#built in funtions

print(issubclass(A,B))
print(issubclass(B,A))


#instance

class A:
	pass
class B(A):
	pass

b = B()
print(isinstance(b,B))
print(isinstance(b,B))


#super functions

class Fruit:
    def __init__(self, fruit):
        print("Fruit type: ", fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')

apple = FruitFlavour()

    