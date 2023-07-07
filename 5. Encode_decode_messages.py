ascii_art = '''

 $$$$$$\                                                           $$$$$$\  $$\           $$\                           
$$  __$$\                                                         $$  __$$\ \__|          $$ |                          
$$ /  \__| $$$$$$\   $$$$$$\   $$$$$$$\  $$$$$$\   $$$$$$\        $$ /  \__|$$\  $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$ |       \____$$\ $$  __$$\ $$  _____| \____$$\ $$  __$$\       $$ |      $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ |       $$$$$$$ |$$$$$$$$ |\$$$$$$\   $$$$$$$ |$$ |  \__|      $$ |      $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$\ $$  __$$ |$$   ____| \____$$\ $$  __$$ |$$ |            $$ |  $$\ $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$  |\$$$$$$$ |\$$$$$$$\ $$$$$$$  |\$$$$$$$ |$$ |            \$$$$$$  |$$ |$$$$$$$  |$$ |  $$ |\$$$$$$$\ $$ |      
 \______/  \_______| \_______|\_______/  \_______|\__|             \______/ \__|$$  ____/ \__|  \__| \_______|\__|      
                                                                                $$ |                                    
                                                                                $$ |                                    
                                                                                \__|                                    

'''

print(ascii_art)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction.lower() == "decode":    # For decoding
        shift_amount *= -1
    elif cipher_direction.lower() != "encode":    # For encoding
        print("\nWrong operation!")
        return
    for char in start_text:    
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")

should_run = True

while should_run:
    direction = input("Type Encode to encrypt, type Decode to decrypt: ")
    text = input("\nType your message: ").lower()
    shift = int(input("\nType the shift number: "))
    shift = shift % 26    # Use modulus operation to traverse the alphabet list circularly
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    wish_to_contd = input("\nType 'yes' to continue and 'no' to terminate: ")
    if wish_to_contd == "no":
        should_run = False
        print('\nBye!')
