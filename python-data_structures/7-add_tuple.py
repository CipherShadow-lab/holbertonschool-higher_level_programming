#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a0 = tuple_a[0] if len(tuple_a) > 0 else 0
    a1 = tuple_a[1] if len(tuple_a) > 1 else 0
    b0 = tuple_b[0] if len(tuple_b) > 0 else 0
    b1 = tuple_b[1] if len(tuple_b) > 1 else 0

    return(a0 + b0, a1 + b1)




#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))