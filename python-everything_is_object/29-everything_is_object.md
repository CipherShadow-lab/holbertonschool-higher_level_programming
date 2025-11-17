
## **Introduction**

Python is often praised for being simple, elegant, and fun to use, however beneath that simplicity lies a powerful model of how data behaves. 
Whether manipulating lists, passing variables into functions or debugging strange behaviour, understanding Python’s concept of identity, types, mutability, and argument passing will transform the way you think about coding. In this post, these concepts are explored with clear explanations, code examples, outputs, and practical implications.

---

## **Identity and Type**

Every Python object has two critical properties:  
Its **identity**, which never changes and its **type** - which defines what kind of object it is.

### Identity

Identity is stored as a memory address. Retrieve it using `id()`:

```python
a = 42
b = 42

print(id(a))
print(id(b))
print(a is b)  # True (small integers reused by Python)
```

**Output (example):**

```python
140736583606656
140736583606656
True
```

### Type

Retrieve type using `type()`:

```python
print(type(a)) #class 'int'
print(type([1, 2, 3]))  #class 'list'
```

Type determines:  
- allowed operations  
- mutability  
- behaviour when passed to functions

---

## **Mutable Objects**

A **mutable object** can be changed in place. This means its contents can change without changing its identity.

Examples:

- lists
- dictionaries
- sets etc


```python
nums = [1, 2, 3]
print(id(nums))

nums.append(4)
print(nums)
print(id(nums)) #same ID -> mutated in place
```

**Output:**

```python
140108048159872
[1, 2, 3, 4]
140108048159872
```

**NOTE:** As shown above, the identity doesn't change. Instead, the object was mutated.

---

## **Immutable Objects**

An **immutable object** cannot be changed after creation. Any “change” results in a **new object**.

Examples:

- int
- float
- str
- tuple
- bool

```python
x = 10
print(id(x))

x = x + 1
print(id(x))`
```

**Output:**

```python
140736583606656
140736583606688
```

Here, Python created a new integer object. This means the old one remained untouched.

Strings work the same:

```python
s = "hi"
print(id(s))

s += "!"
print(id(s))`
```

Again, the output will show a new ID each time.

---

## **Why this Matters (and How Python Treats Them Differently)**

Mutability affects:

### 1. **Performance**
Mutable objects avoid creating copies - making them faster for repeated updates (e.g., list appends).

### 2. **Memory usage**
Immutable objects are reused by Python (E.g. strings, integers).

### 3. **Behaviour in data structures**
Immutable types can be dictionary keys, whereas mutable types cannot.

### 4. **Unexpected shared references**

Mutability can lead to surprises:

```python
a = [1, 2, 3]
b = a

b.append(4)
print(a)  #output: [1, 2, 3, 4]
```

Here, `a` changed because both variables point to the same object.

---

## **How Function Arguments Are Passed

When a function in Python is called and passed as a variable, Python doesn't copy the value.
Instead, Python gives the function a **reference** to the same object that is passed in.

For example:

Imagine having a cup of juice:
- Cup = the object (list, int etc)
- Label (on the cup) = the variable name

When this is passed to a function, the function is handed the label that points to the same cup ;)

This means:

- Mutable objects (e.g. lists) - can change the cup. So if the function modifies it, the *original* cup changes.
- Immutable objects (e.g. integers, strings) - If the function changes it, then Python will *create a new cup*.

### Mutable example: list

```python
def add_item(my_list):
	my_list.append(99)

nums = [1, 2, 3]
add_item(nums)

print(nums)
```

**Output:**

```python
[1, 2, 3, 99]
```

Here:
- `nums` is a label pointing to a list
- `my_list` is the new label pointing to the same list
- `.append()` changes the list itself

So, both labels see the change!
 

---

### Immutable example: int

```python
def add_one(x):
	x = x + 1
	print("Inside Function:", x)
	
num = 10
add_one(num)
print("Outside Function:", num)
```

Here:
- `num` is the label pointing to integer `10`
- `x` is the new label pointing to the same integer `10`

BUT integers cannot change so:

- `x = x + 1` creates a new integer object `11`
- `x` now points to `11`
- `num` still points to `10`

**Output:**

```python
Inside Function: 11
Outside Function: 10
```

In summary, Python passes a reference to the object. Whether the original changes depends on whether the object itself can change. 


## **Conclusion**

Understanding identity, type, mutability, immutability, and function argument behavior is essential for writing robust Python code. These concepts influence performance, memory usage, debugging, and the behavior of nearly every line of code that is written.
