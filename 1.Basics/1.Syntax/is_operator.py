# Example 1: Same object
list1 = [1, 2, 3]
list2 = list1  # list2 now refers to the exact same list object as list1

print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"Are list1 and list2 the same object? {list1 is list2}")
# Output: Are list1 and list2 the same object? True

list2.append(4) # Modifying list2 also modifies list1 because they are the same object
print(f"list1 after modifying list2: {list1}")
print(f"list2 after modifying list2: {list2}")


# Example 2: Different objects with the same value
list3 = [1, 2, 3]
list4 = [1, 2, 3] # list4 is a new list object, even though its value is the same as list3

print(f"\nlist3: {list3}")
print(f"list4: {list4}")
print(f"Do list3 and list4 have the same value? {list3 == list4}")
# Output: Do list3 and list4 have the same value? True
print(f"Are list3 and list4 the same object? {list3 is list4}")
# Output: Are list3 and list4 the same object? False


# Example 3: Identity for small integers and strings (interning)
# Python often "interns" small integers and short strings for optimization.
# This means that identical small integer/string literals might refer to the same object.

a = 10
b = 10
print(f"\na: {a}")
print(f"b: {b}")
print(f"Are a and b the same object? {a is b}") # Usually True for small integers

s1 = "hello"
s2 = "hello"
print(f"\ns1: {s1}")
print(f"s2: {s2}")
print(f"Are s1 and s2 the same object? {s1 is s2}") # Usually True for short, interned strings

s3 = "a very long string that might not be interned automatically"
s4 = "a very long string that might not be interned automatically"
print(f"\ns3: {s3}")
print(f"s4: {s4}")
print(f"Are s3 and s4 the same object? {s3 is s4}") # Might be False, depending on Python version/implementation


# "is not" is simply a negation of "is"