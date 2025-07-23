a = 10
b = 13

# BITWISE AND
c = a & b 
print(c)

print(format(a, 'b'))
print(format(b, 'b'), "AND")
print(format(c, 'b'), "\n\n")

# BITWISE OR
c = a | b
print(format(a, 'b'))
print(format(b, 'b'), "OR")
print(format(c, 'b'), "\n\n")

# BITWISE XOR
c = a ^ b
print(format(a, 'b'))
print(format(b, 'b'), "XOR")
print(format(c, 'b'), "\n\n")

# BITWISE NOT
c = ~b
print(format(b, 'b'), "NOT")
print(format(c, 'b'), "\n\n")

# BITWISE LEFT SHIFT, (shifts bits of a, b times to the left)
c = a << b
print(format(a, 'b'))
print(format(b, 'b'), "LEFT SHIFT")
print(format(c, 'b'), "\n\n")

# BITWISE RIGHT SHIFT, (shifts bits of b, a times to the right)
c = a >> b
print(format(a, 'b'))
print(format(b, 'b'), "RIGHT SHIFT")
print(format(c, 'b'), "\n\n")
