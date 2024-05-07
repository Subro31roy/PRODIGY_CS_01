def caesar_cipher(text, shift, operation):

    shift = shift % 26
    if operation == 'decrypt':
        shift = -shift

    
    result = []

    for char in text:
        if char.isalpha():  
            start = ord('a') if char.islower() else ord('A')
            offset = (ord(char) - start + shift) % 26
            result.append(chr(start + offset))
        else:
           
            result.append(char)

    return ''.join(result)

def main():
    print("Welcome to the Caesar Cipher Program!")
    text = input("Please enter the text: ")
    shift = int(input("Please enter the shift value: "))
    
    
    while True:
        operation = input("Do you want to 'encrypt' or 'decrypt'? ").lower()
        if operation in ['encrypt', 'decrypt']:
            break
        print("Invalid operation. Please choose 'encrypt' or 'decrypt'.")

    result = caesar_cipher(text, shift, operation)
    print(f"The {operation}ed text is: {result}")

if __name__ == "__main__":
    main()
