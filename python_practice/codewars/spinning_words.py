#for five or more words returns them reversed

def spin_words(sentence):
    # Your code goes here
    old_list = sentence.split()
    new_list = []
    for i in range(len(old_list)):
        if len(old_list[i]) > 4:
            reversed = old_list[i][::-1]
            new_list.append(reversed)
        else:
            new_list.append(old_list[i])

    return " ".join(new_list)

print(spin_words("Hey fellow warriors"))





# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
# spinWords( "This is a test") => returns "This is a test" 
# spinWords( "This is another test" )=> returns "This is rehtona test"