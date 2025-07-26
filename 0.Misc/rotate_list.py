lst = [1,2,3,4,5,6]

n = int(input("Enter the Rotate Iterations: "))

new_lst = lst[n:] + lst[:n]

print(lst)
print(new_lst)