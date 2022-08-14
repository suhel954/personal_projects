def alphabet_position(text):
    text = text.lower()
    string = ''

    for i in text:
        #checking for alphabets only
        if i.isalpha():
            #ord gives the ascii value of the lower case letter which should be subtracted by 96 to get order of letter
            string += str(ord(i) - 96)
            string += " "
        
    return string.strip()   #remove whitespace with strip()

