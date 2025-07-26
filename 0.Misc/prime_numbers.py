num = int(input("Find Prime Numbers upto: ")) + 1

for i in range(3, num):
    is_prime = True
    for j in range(2, i): 
        if i % j == 0: 
            is_prime = False
            break
    if is_prime: 
        print(i, end = " ")