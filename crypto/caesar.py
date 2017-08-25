alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def alphabet_position(letter):
    return alphabet.index(letter.lower())

def rotate_character(char, rot):
    if not char.isalpha():
        return char
    else:
        num = alphabet_position(char)   #index of char 
        num = num + rot                 #index of char moved over rot
        alpha = alphabet[num % 26]      #num coverted to letter using alphabet 
        return alpha

#print(rotate_character('a',13))

def encrypt(text, rot):
    output = ''
    for a in text:
        output += rotate_character(a, rot)
    return output 

print(encrypt("LaunchCode", 13))