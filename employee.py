#наследование
from distutils import extension
from oop import Person

class Employee(Person):
    years_experence = 0
    program_langs = []

    def __init__(self, experience=0, program_langs=[], **kwargs): # *args(список) **kwargs(словарь) 
        Person.__init__(self, **kwargs)
        self.years_experence = experience
        self.program_langs = program_langs
        print(experience)

dima_employee = Employee(first_name="Dima", last_name="Yefimov", experience=8, program_langs=["Python"])
petro_employee = Employee(first_name="Petro", last_name="Petrenko", experience=10, program_langs=["PHP"])

print(dima_employee.program_langs)

print(petro_employee.program_langs)


#инкапсуляция

#__function_and_varieble         "prived"

#new class(class extension)      "public"


#полиморфизм
#возможность использовать одинаковые имена в разных классах и в дочерних классах


