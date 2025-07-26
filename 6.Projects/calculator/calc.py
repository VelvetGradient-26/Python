import art

logo = art.calci
store = 0

def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    return a / b

operations = { 
    '+': add, 
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def operation(character): 
    match(character): 
            case '+': 
                store = add(first_number, second_number)
                print(store)
            case '-':
                store = subtract(first_number, second_number)
                print(store)
            case '*': 
                store = multiply(first_number, second_number)
                print(store)
            case '/':
                store = divide(first_number, second_number)
                print(store)
            case _: 
                print("Enter a valid operation")


while True: 
    op = input("Pick an operation (+, -, *, /): ")
    first_number = float(input("Enter the first Number: "))
    second_number = float(input("Enter the second Number: "))

    operation(op)

    choice = input((f"Do you want to continue calculation with {store} or quit? (Type 'yes' or 'no)")).lower()

    if choice == "yes": 
        first_number = store
        second_number = float(input("Enter Second Number: "))
    elif choice == "no": 
        print(f"Final Result is Store: {store}")
        break
    else: 
        print("Enter Valid Input!")
    
                        