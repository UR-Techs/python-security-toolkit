def caesar_encrypt(shift, user_message):
    encrypted_text = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in user_message:
        if char.isalpha():
            
            if char.isupper():
                char_index = alphabet.find(char.lower())
                new_index = (char_index+shift)%26
                encrypted_text += alphabet[new_index].upper()
            else:
                char_index = alphabet.find(char)
                new_index = (char_index+shift)%26
                encrypted_text += alphabet[new_index]

        else:
            encrypted_text += char
        
    print(f"Original Text : {user_message}")
    print(f"Encrypted Text : {encrypted_text}")

def caesar_decrypt(shift, encrypted_message):
    decrypted_text = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in encrypted_message:
        if char.isalpha():
            if char.isupper():
                char_index = alphabet.find(char.lower())
                new_index = (char_index-shift)%26
                decrypted_text += alphabet[new_index].upper()
            else:
                char_index = alphabet.find(char)
                new_index = (char_index-shift)%26
                decrypted_text += alphabet[new_index]
        else:
            decrypted_text += char
        
    print(f"Original Text : {encrypted_message}")
    print(f"Decrypted Text : {decrypted_text}")

def caesar_brute_force(encrypted_message):
    for shift in range(1,27):
        decrypted_text = ""
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for char in encrypted_message:
            if char.isalpha():
                if char.isupper():
                    char_index = alphabet.find(char.lower())
                    new_index = (char_index-shift)%26
                    decrypted_text += alphabet[new_index].upper()
                else:
                    char_index = alphabet.find(char)
                    new_index = (char_index-shift)%26
                    decrypted_text += alphabet[new_index]
            else:
                decrypted_text += char
        print()
        print(f"Shift: {shift}")
        print(f"Original Text : {encrypted_message}")
        print(f"Decrypted Text : {decrypted_text}")
        print()
        
    

def menu():
   
    while True:
        print()
        print("Do you Want to encrypt the text or Decrypt the Text?")
        print("Press 1 , 2 , 3 or 4")
        print("1. Encrypt\n2. Decrypt\n3. Brute Force\n4. Exit\n")
    
        user_choice = int(input())
        print()

        if user_choice == 1:
            user_message = input("Enter a message to Encrypt: ")
            shift = int(input("Enter a number to use as a shift: "))
            caesar_encrypt(shift, user_message)
            
        elif user_choice == 2:
            user_message = input("Enter a message to Decrypt: ")
            shift = int(input("Enter a number to use as a shift: "))
            caesar_decrypt(shift, user_message)

        elif user_choice == 3:
            user_message = input("Enter a message to Decrypt: ")
            caesar_brute_force(user_message)
        
        elif user_choice == 4:
            print("Exiting the program. BYE!")
            break
            

menu()