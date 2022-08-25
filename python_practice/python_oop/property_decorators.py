class Employee:

    def __init__(self,first,last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # @fullname.setter
    # def fullname(self,name):
    #     first, last = name.split(' ')
    #     self.first = first
    #     self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

    @property     #property decorator   
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)



emp1 = Employee('John', 'Smith')

emp1.first = 'Jim'
emp1.fullname = 'Suhel Shaikh'

print(emp1.first)
print(emp1.email)  #can be accessed as an attribute as property decorater was used
print(emp1.fullname)