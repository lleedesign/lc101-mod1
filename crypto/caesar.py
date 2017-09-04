from helpers import get_alphabet, alphabet_position, rotate_character

def encrypt(text, rot):
    output = ''
    for a in text:
        output += rotate_character(a, rot)
    return output 

#print(encrypt("LaunchCode", 13))       #for testing

def main():
    text = input("Type a message: ")    
    rot = int(input("Rotate by: "))
    print(encrypt(text, rot))

if __name__ == "__main__":
    main()