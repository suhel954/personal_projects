def expanded_form(num):
    #can multiply string '0' to the end
    result = []
    for index, digit in enumerate(str(num)[::-1]):
        if int(digit) != 0:
            #digit is a string so adding '0' next to it
            result.append(digit + ('0'*index))
        
    return ' + '.join(result[::-1])

print(expanded_form(70304))




