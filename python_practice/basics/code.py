# user_age = input("Enter your age: ")
# years = int(user_age)

# months = years*12

# print(f"The age of the user is months {months}")





# local = {'Rolf'}
# abroad = {'Bob', 'Anne'}

# friends = local.union(abroad)

# print(friends)

# friends = ['Rolf', 'Rob', 'Bob']

# print('Bob' in friends)

# movies_watched = {"The Matrix", "Green Book", "Her"}
# user_movie = input("Enter something you've watched recently: ")

# if user_movie in movies_watched:
#     print(f"I have watched {user_movie} too")

# else:
#     print("I havent watched that yet")


# number = 7

# user_input = input("Enter 'y' if you would like to play: ")

# if user_input in ('y', 'Y'): #using a tuple to provide options
#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("You guessed correctly")
#     elif abs(number - user_number) == 1:
#         print('You were off by one.')
#     else:
#         #print(f"Sorry, {user_number} is not the correct guess.")
#         print('Sorry, {} is not the correct guess'.format(user_number))

#list comprehension


# numbers = [1,3,5]
# doubled = [x*2 for x in numbers]

# friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
# start_s = [friend for friend in friends if friend.startswith("S")] #friend is the value we need from the for loop
# print(start_s)



# friends_dict = [
#     {'name':"Rolf", 'age': 24},
#     {'name':"Adam", 'age': 54},
#     {'name':"Anne", 'age': 74},
# ]

# print(friends_dict[1]["age"])


# #x, y = 5,11
# t = 5,11
# x,y =t


# student_attend = {"Rolf": 96, "Bob": 80, "Anne": 100}

# for student, attend in student_attend.items():
#     print(f"{student}: {attend}")

# print(list(student_attend.items()))

# to ignotre values use '_'

# person = ('Bob', 24, 'Mechanic')

# name, _, profession = person


#first one and then the rest will be in the last list
# head, *tail = [1,2,3,4,5]


#default parameter values must go at the end
# def add(x,y=8): 
#     print(x+y)

# add(x=5)

#lambda function, short function without giving them a name

# add = lambda x,y: x+y #same as the add function previously

# print(add(5,7))

# def double(x):
#     return x*2

# sequence = [1,3,5,9]
# doubled = [double(x) for x in sequence]
# doubled = list(map(double, sequence)) # add a list cuz map returns a map object
#  # goes over each element and applies the function


#dictionary comprehension

# users = [
#     (0, 'Bob', 'password'),
#     (1, 'Rolf', 'passworddawd'),
#     (2, 'Jose', 'passwwdaord'),
#     (3, 'username', '22password'),
# ]

# username_mapping = {user[1]: user for user in users}

# username_input = input("username: ")
# password_input = input("password: ")

# _, username, password = username_mapping[username_input]

# if password_input == password:
#     print("Correct password")
# else:
#     print("Wrong Password")

#print(username_mapping)

student = {
    'name':'Jose',
    'school': 'Computing',
    'grades' : (66,77,88),
}

def average_grade(data):
    grades = data['grades']
    return sum(grades)/len(grades)


def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student['grades'])
        count += len(student['grades'])
    
    return total/count


