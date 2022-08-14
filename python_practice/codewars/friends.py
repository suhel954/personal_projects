def friend(x):
    my_friends = []
    #Code
    for i in range(len(x)):
        if len(x[i]) == 4:
            my_friends.append(x[i])
            i += 1
        else:
            continue
            
    return list(dict.fromkeys(my_friends))


print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))
