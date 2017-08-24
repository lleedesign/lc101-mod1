def get_initials(fullname):
    separated_name = fullname.split(" ")
    first_letter = []
    for item in separated_name:
        #first_letter.append(item[0:2])   THIS OR lines 6&7
        fullname = item[0:1]
        first_letter.append(fullname)
    glue = ''
    total = glue.join(first_letter)
    total = total.upper()
    return total
    
def main():
    fullname = input("What is your full name?")    
    print(get_initials(fullname))

if __name__ == '__main__':
    main()   