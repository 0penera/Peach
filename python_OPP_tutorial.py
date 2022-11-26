#python object_oriented_programming


class Employee:
    
    num_of_emp = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
        Employee.num_of_emp += 1
    
    @property    
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last
        
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.Last = None
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    def __repr__(self):
        return "Employee({}, {}, {})"\
            .format(self.first, self.last, self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    # def __len__(self):
    #     return len(self.fullname())
        
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('_')
        return cls(first, last, pay)
        
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
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
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
        
        
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Developer('Test', 'User', 60000, 'java')

mgr_1 = Manager('sue', 'smith', 90000, [emp_1])

print(emp_1 + emp_2)
print('test'.__len__())
# print(len(emp_1))

emp_1.fullname = 'Corey ss'

del emp_1.fullname

# emp_1.first = 'a'
print(emp_1.first)
print(emp_1.email)
# repr(emp_1)
# str(emp_1)

# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Employee))
# print(isinstance(mgr_1, Developer))
# print(issubclass(Manager, Employee))
# print(issubclass(Developer, Employee))
# print(issubclass(Manager, Developer))

# print(mgr_1.email)

# mgr_1.add_emp(emp_2)
# mgr_1.print_emps()

# print(emp_1.prog_lang)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(help(Developer))

# import datetime
# my_date = datetime.date(2022, 11, 13)

# print(Employee.is_workday(my_date))

# emp_str_1 = 'john_doe_70000'
# emp_str_2 = 'steve_smith-30000'
# emp_str_3 = 'jane_doe_90000'

# first, last, pay = emp_str_1.split('_')
# new_emp_1 = Employee(first, last, pay)

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# Employee.set_raise_amount(1.05)
# Employee.raise_amount(1.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# # print(emp_1)
# print(emp_2)

# print(emp_1.email)
# print(emp_2.email)

# print('{} {}'.format(emp_1.first, emp_1.last))
# print(emp_1.fullname())

# print(Employee.fullname(emp_1))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(Employee.__dict__)
# print(emp_1.__dict__)

# Employee.raise_amount = 1.05
# emp_1.raise_amount = 1.05

# print(emp_1.__dict__)
# print(emp_2.__dict__)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)

# print(Employee.num_of_emp)