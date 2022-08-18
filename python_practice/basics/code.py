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

# student = {
#     'name':'Jose',
#     'school': 'Computing',
#     'grades' : (66,77,88),
# }

# def average_grade(data):
#     grades = data['grades']
#     return sum(grades)/len(grades)


# def average_grade_all_students(student_list):
#     total = 0
#     count = 0
#     for student in student_list:
#         total += sum(student['grades'])
#         count += len(student['grades'])
    
#     return total/count




#function *args creates a tuple of arguments
#multiple arguments in a single variable as a tuple


# def multiply(*args):
#     print(args)
#     total = 1
#     for arg in args:
#         total = total * arg

#     return total

# # print(multiply(1,2,5))

# # def add(x,y):
# #     return x+y

# # nums = [5,5]
# # print(add(*nums)) #'*' adds each value for each parameter

# def apply(*args, operator):
#     if operator == "*":
#         return multiply(*args)
#     elif operator == '+':
#         return sum(args)
#     else:
#         return "No valid operator provided to apply()."

# print(apply(1,2,3,4,56,7, operator="*"))


#'**' collects keyword arguments and stores it in a dictionary
# def named(**kwargs):
#     print(kwargs)

# named(name='Bob', age=25)

# def named(name, age):
#     print(name,age)

# details = {'name':'Bob', 'age':'25'}

# named(**details)


# def named(**kwargs):
#     print(kwargs)

# def print_nicely(**kwargs):
#     named(**kwargs)
#     for arg, value in kwargs.items():
#         print(f"{arg}: {value}")

# print_nicely(name='Bob', age=25)

# #to store arguments and name arguments:
# def both(*args, **kwargs):
#     print(args)
#     print(kwargs)

# both(1,3,5, name='Bob', age=25)

#object orient programming




# class Student:

#     def __init__(self, name, grades):   #init is a method
#         self.name = name
#         self.grades = grades
#     def average(self):
#         return sum(self.grades)/len(self.grades)



# student = Student('Bob', (90,90,93,78,89))
# print(student.average())

# class Person:   #here Person object is created by calling the class
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):   #when you want to convert your object into a string
#         return f'hello {self.name}, {self.age}'

#     def __repr__(self):  #unambigious representation of the object
#         return f'<Person({self.name}, {self.age})>'

# bob = Person('Bob', 25)
# print(bob)

# class Store:
#     def __init__(self,name):
#         self.name = name
#         self.items = []

#     def add_item(self,name,price):
#         item = {'name':name, 'price':price}
#         self.items.append(item)

#     def stock_price(self):
#         return sum([item['price'] for item in self.items])




# class ClassTest:
#     def instance_method(self):
#         print(f'Called Instance_method of {self}')

#     @classmethod
#     def class_method(cls):
#         print(f"Called class_method of {cls}")

#     @staticmethod    #independent function that does not take any parameters of class
#     def static_method():
#         print("Called static_method.")

# test = ClassTest()

# test.instance_method()

# ClassTest.class_method



# class Book:
#     TYPES = ('hardcover','paperback')

#     def __init__(self, name, book_type, weight):
#         self.name = name
#         self.book_type = book_type
#         self.weight = weight

#     def __repr__(self):
#         return f"Book {self.name}, {self.book_type}, weighing {self.weight} g"

#     @classmethod
#     def hardcover(cls, name, page_weight):
#         return cls(name, cls.TYPES[0], page_weight + 100)

#     @classmethod
#     def paperback(cls, name, page_weight):
#         return Book(name, Book.TYPES[1], page_weight)


# book = Book.hardcover('Harry Potter', 1500)

# light = Book.paperback('Harry Potter', 600)

# print(book)
# print(light)


# class Store:
#     def __init__(self, name):
#         self.name = name
#         self.items = []

#     def add_item(self, name, price):
#         self.items.append({
#             'name': name,
#             'price': price
#         })

#     def stock_price(self):
#         total = 0
#         for item in self.items:
#             total += item['price']
#         return total

#     @classmethod
#     def franchise(cls, store):
#         # Return another store, with the same name as the argument's name, plus " - franchise"
#         new_store = Store(store.name + ' - franchise')
#         return new_store

#     @staticmethod
#     def store_details(store):
#         # Return a string representing the argument
#         # It should be in the format 'NAME, total stock price: TOTAL'
#         details = '{}, total stock price: {}'.format(store.name, store.stock_price())
#         return details

# store = Store("Test")
# store.add_item('Keyboard', 160)

# print(Store.store_details(store))


# class Device:
#     def __init__(self, name, connected_by):
#         self.name = name
#         self.connected_by = connected_by
#         self.connected = True

#     def __str__(self):
#         return f'Device {self.name!r} {self.connected_by}'

#     def disconnect(self):
#         self.connected = False
#         print('Disconnected')


# class Printer(Device):
#     def __init__(self, name, connected_by, capacity):
#         super().__init__(name, connected_by)   #call the parent class
#         self.capacity = capacity
#         self.remaining_pages = capacity

#     def __str__(self):
#         return f'{super().__str__()} ({self.remaining_pages} pages remaining)'


#     def print(self,pages):
#         if not self.connected:
#             print('Your printer is not connected')
#             return
#         print(f'Printing {pages} pages.')
#         self.remaining_pages -= pages


# printer = Printer('Printer', 'USB', 500)
# printer.print(20)

# print(printer)

# printer.disconnect()
# printer.print(30)

# class BookShelf:
#     def __init__(self, books: List[Book]):
#         self.books = books

#     def __str__(self):
#         return f'Bookshelf has currently {len(self.books)} books'

# class Book:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self) -> str:
#         return f'Books {self.name}'

# book1 = Book('Harry Potter')
# book2 = Book('Python')
# shelf = BookShelf(book1, book2)

# print(book1)
# print(shelf)

# from typing import List

# def list_avg(sequence: list) -> float: #type hinting and provided what kind of i/o should be there
#     return sum(sequence)/len(sequence)

# list_avg(123)


