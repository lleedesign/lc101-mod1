sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."

def count_char(sentence):
    BOO = {}
    for letter in sentence:
        if letter in BOO:
            BOO[letter] += 1
        else:
            BOO[letter] = 1

    for key, value in BOO.items():
        print(key, value) 

count_char(sentence)
