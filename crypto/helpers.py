def get_alphabet():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return alphabet

def alphabet_position(letter):
    alphabet = get_alphabet()
    return alphabet.index(letter.lower())

def rotate_character(char, rot):
    alphabet = get_alphabet()
    if not char.isalpha():              #only deal with alpha characters
        return char
    else:
        is_upper = False
        if char >= 'A' and char <= 'Z':
            is_upper = True
        num = alphabet_position(char)   #index of char 
        num = num + rot                 #index of char moved over rot
        alpha = alphabet[num % 26]      #num coverted to letter using []
        if is_upper:
            return alpha.upper()
        return alpha