from calendar import weekday
import datetime


class Employee:

    #class variable
    num_employees = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)

    def __repr__(self) -> str:
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)

    def __str__(self) -> str:
        return '{} - {}'.format(self.fullname(), self.email)


    # @classmethod
    # def set_raise_amt(cls, amount):
    #     cls.raise_amount = amount

    # @classmethod
    # def from_string(cls, emp_string):
    #     first, last, pay = emp_string.split('-')
    #     return cls(first, last, pay)

    # @staticmethod
    # def is_workday(day):
    #     if day.weekday() == 5 or day.weekday() == 6:
    #         return False
    #     return True


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)


    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)


    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())



dev1 = Developer('Suhel','Shaikh',50000, 'python')
dev2 = Developer('Sohel','Shssikh',60000, 'java')
mgr_1 = Manager('Sur', 'Alba', 90000, [dev1, dev2])


print(issubclass(Developer, Manager))

print(dev1)

print(dev1.__repr__())






    
