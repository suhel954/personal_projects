#get a number and create countdown

list = [0, -3, 6, 7]

#positive number
#negative number
#if zero

#positive
bump = 1
zero = 0
index = 0
for numbers in list:
    firstNumber = list[index]
    print(firstNumber)
    index = index + 1

    #positive
    if firstNumber > 0:
        output = firstNumber - bump
        while output >=0:
            print(output)
            output = output - 1
            if output == zero:
                print(output)
                break
    #negative
    if firstNumber < 0:
        output = firstNumber + bump
        while output <=0:
            print(output)
            output = output + 1
            if output == zero:
                print(output)
                break

    #zero
    if firstNumber == zero:
        print(firstNumber)



