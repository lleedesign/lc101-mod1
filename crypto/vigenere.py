from helpers import get_alphabet, alphabet_position, rotate_character

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