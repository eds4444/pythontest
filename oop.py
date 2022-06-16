class Person():
    first_name =""
    last_name =""

    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name  

    def get_name(self):
        return self.first_name + ' ' + self.last_name + ' name'      
        

dima_person = Person(first_name="Dima", last_name="Yefimov")
petro_person = Person(first_name="Petro", last_name="Petrenko")

print(dima_person.first_name)
print(dima_person.last_name)
print(dima_person)
print(dima_person.get_name())

print(petro_person.first_name)
print(petro_person.last_name)
print(petro_person)
print(petro_person.get_name())
