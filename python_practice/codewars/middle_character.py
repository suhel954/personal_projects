def get_middle(s):
    if len(s) % 2 == 0:
        mid = int(len(s)/2)
        #mid_letter1 = s[mid - 1]
        #print(mid_letter1)
        #mid_letter2 = s[mid]
        return s[mid - 1] + s[mid]
    else:
        mid = int((len(s) + 1)/2)
        return s[mid-1]



# Kata.getMiddle("test") should return "es"

# Kata.getMiddle("testing") should return "t"

# Kata.getMiddle("middle") should return "dd"

# Kata.getMiddle("A") should return "A"
