# for more details for MRO check this link -> http://www.srikanthtechnologies.com/blog/python/mro.aspx


#MRO - Method Resolution Order
class A:
    num = 10


class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass


obj = D ()
print(D.num)
print (D.mro())   # OR print (D.__mro__)


class A:
    num = 10

class B:
    pass

class C(A,B):
    num = 1

class D(C,B):
    pass

print (D.mro())


