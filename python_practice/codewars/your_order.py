#copied from hevalhazalkurt github
def order(sentence):
    words = []
    #giving the range from 1 to 10
    for i in range(1,10):
        #splitting the sentence into a list of words
        for word in sentence.split():
            #checking if i can be found in the list, as i starts from 1, it will check for string '1' in the list
            if str(i) in word:
                words.append(word)
    return " ".join(words)




        
        


