
alphabet = "abcdefghijklmnopqrstuvwxyz"
output = ""


choice = input("Encrypt or Decrypt").lower()
if choice=="encrypt":
    message = input("Enter your message:")
    shift = int(input("Enter the shift :"))


    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + shift) % 26
            output += alphabet[new_index]
        else:
            output+= char

    print(f"Encrypted message: {output}")
else:
    message = input("Enter your message:")
    shift = int(input("Enter the shift :"))

    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index - shift) % 26
            output += alphabet[new_index]
        else:
            output+= char

    print(f"Encrypted message: {output}")
    # this is just a test
