alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def alphabet_position(letter):
    return alphabet.index(letter.lower())

def rotate_character(char, rot):
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

#print(rotate_character('a',13))        #for testing

def encrypt(text, key):
    output = ''
    ind = 0
    for letter in text:
        rot = alphabet_position(key[ind % len(key)])
        if letter.isalpha():
            ind = ind + 1
        output += rotate_character(letter, rot)
    return output 

#print(encrypt("LaunchCode", 13))       #for testing

def main():
    #text = input("Type a message: ") 
    text = "The crow flies at midnight!"
    #key = "input("Encryption key: ")"
    key = "boom"
    print(encrypt(text, key))

if __name__ == "__main__":
    main()

#Uvs osck rmwse bh auebwsih!