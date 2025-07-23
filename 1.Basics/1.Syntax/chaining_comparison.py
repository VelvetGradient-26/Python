age = 25

# Instead of:
# if age > 18 and age < 65:
#     print("Adult working age")

# Use chaining:
if 18 < age < 65:
    print("Adult working age")

# Another example with inclusive bounds:
temperature = 22.5
if 20 <= temperature <= 25:
    print("Temperature is comfortable.")

# checkinug if multiple values are equal
x = 10
y = 10
z = 10

# Instead of:
# if x == y and y == z:
#     print("All values are equal")

# Use chaining:
if x == y == z:
    print("All values are equal")

a = 5
b = 5
c = 7
if a == b == c:
    print("All equal")
else:
    print("Not all equal")

# Checking for an increasing or decreasing sequence 
num1 = 5
num2 = 10
num3 = 15

# Strictly increasing
if num1 < num2 < num3:
    print("Numbers are in strictly increasing order.")

num4 = 20
num5 = 15
num6 = 10

# Strictly decreasing
if num4 > num5 > num6:
    print("Numbers are in strictly decreasing order.")

# comparison chaining doesn't work with != operator 
a = 1
b = 2
c = 1

# This does NOT mean a, b, and c are all different.
# It means (a != b) AND (b != c).
if a != b != c:
    print("This might be misleading if you expect all to be unique.")
    # Output: This might be misleading if you expect all to be unique.
    # Because (1 != 2) is True AND (2 != 1) is True.
    # a and c are the same, but the chained comparison doesn't catch that.

# If you want to check if all values are unique, it's better to use:
if len(set([a, b, c])) == 3:
    print("All values are unique.")
else:
    print("Not all values are unique.")