def vigenere_encrypt(user_message,message_key):
    encrypted_message = ""
    key_array = []
    encrypted_text = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for word in user_message:
        if word.isalpha():
            encrypted_message += word


    while len(key_array) < len(encrypted_message):
        for char in message_key:
            if len(key_array) < len(encrypted_message):
                key_array.append(char)
            
            
    index = 0

    for char in user_message:
        if char.isalpha():
            
            if char.isupper():
                char_index = alphabet.find(char.lower())
                key_index = alphabet.find(key_array[index].lower())
                new_index = (char_index+key_index)%len(alphabet)
                encrypted_text += alphabet[new_index].upper()
                
                
            else:
                char_index = alphabet.find(char)
                key_index = alphabet.find(key_array[index].lower())
                new_index = (char_index+key_index)%len(alphabet)
                encrypted_text += alphabet[new_index]

            index += 1
        
        else:
            encrypted_text += char
        
    print(encrypted_text)


def vigenere_decrypt(user_message, message_key):
    decrypted_message = ""
    key_array = []
    decrypted_text = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in user_message:
        if char.isalpha():
            decrypted_message += char


    while len(key_array) < len(decrypted_message):
        for char in message_key:
            if len(key_array) < len(decrypted_message):
                key_array.append(char)
            
            
    index = 0

    for char in user_message:
        #print(char , index)
        if char.isalpha():
            
            if char.isupper():
                char_index = alphabet.find(char.lower())
                key_index = alphabet.find(key_array[index].lower())
                new_index = (char_index-key_index)%len(alphabet)
                decrypted_text += alphabet[new_index].upper()                
                
            else:
                char_index = alphabet.find(char)
                key_index = alphabet.find(key_array[index].lower())
                new_index = (char_index-key_index)%len(alphabet)
                decrypted_text += alphabet[new_index]
            index += 1
        
        else:
            decrypted_text += char
        
    print(decrypted_text)

user_message = input("Please enter a message: ")
message_key = input("Please enter a key: ")



vigenere_encrypt(user_message,message_key)