'''
The caesar function will be used to encrypt or decrypt user input.

@parameters:
    text = string provided as encrypt or decrypt text.
    shift = number that is use to perform an alphabetically position shift in the list.
    operation = string letter "e" for encrypt and "d" for decrypt.

@return:
    if operation is "e" then the function will return the encrypted text.
    if operation is "d" then the function will return the decrypted text.
'''
def caesar(text, shift, operation):    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Your code goes here
    try:
        shift = int(shift)
        if shift < 0 or shift > 25:
            return "invalid shift"
    except ValueError:
        return "invalid shift"
    
    if operation not in ["e", "d"]:
        return "invalid option"
    
    result = ""
    
    for character in text:
        if character.isalpha():
            character = character.lower()
            
            if operation == "e": 
                shifted_index = (alphabet.index(character) + shift) % 26
            elif operation == "d": 
                shifted_index = (alphabet.index(character) - shift) % 26
            
            shifted_char = alphabet[shifted_index]
            result += shifted_char
        else:
            result += character
    
    return result