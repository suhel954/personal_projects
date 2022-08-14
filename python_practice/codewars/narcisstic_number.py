def narcissistic(value):
    for i in range(len(value)):
        total = 0
        value_string = str(value)
        num = value[i]**len(value_string)
        total = total + num
    if total == value:
        return '{} is narcissistic'.format(value)

    else:
        return '{} is not narcissistic'.format(value)






