#two employees, create a call for first name, last name, pay and email

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@email.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('Suhel', 'Shaikh', 50000)

print(emp1.email)
print(emp1.fullname())