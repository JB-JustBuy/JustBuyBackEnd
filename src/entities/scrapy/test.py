from itertools import product

test  = {
    'name1': ['001', '002'],
    'rash1': ['12', "3"]
}
a = [dict(zip(test, v)) for v in product(*test.values())]
print(a)