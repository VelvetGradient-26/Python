letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def encrypt(message, shift): 
    encrypted_message = ""

    for char in message: 
        if char not in letters: 
            encrypted_message += char
        else: 
            idx = letters.index(char) + shift
            idx = idx % 26
            encrypted_message += letters[idx]
    
    return encrypted_message

def decrypt(message, shift): 
    decrypted_message = ""

    for char in message: 
        if char not in letters: 
            decrypted_message += char
        else: 
            idx = letters.index(char) - shift
            idx = idx % 26
            decrypted_message += letters[idx]
    
    return decrypted_message

def caesar(message, shift, direction): 
    processed_message = ""

    if direction == 'decode':
        shift *= -1

    for char in message: 
        if char not in letters: 
            processed_message += char
        else: 
            idx = letters.index(char) + shift
            idx = idx % 26
            processed_message += letters[idx]
    
    return processed_message


while True: 
    direction = input("\nType 'encode' to encrypt the message or 'decode' to decrypt the message\nType 'Quit' to exit\n").lower()
    if direction == 'quit':
        break

    message = input("Enter your message: ")
    shift = int(input("Enter the shift number: "))

    if direction == 'encode':
        encoded = encrypt(message, shift)
        print("Encrypted Message is:\n", encoded)
    
    elif direction == 'decode':
        decoded = decrypt(message, shift)
        print("Decrypted Message is:\n", decoded)

    else: 
        print("Bye Bye")
        print("You gave the wrong prompt, enter a correct prompt")
    
