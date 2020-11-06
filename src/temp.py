class A(object):
    value = 10

class B(A):
    value = 1

b = B()
print(isinstance(b, A))