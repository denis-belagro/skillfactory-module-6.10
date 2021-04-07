class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def tell(self):
       print('«{0}, г.{1},'.format(self.name, self.city), end=" ")


class Guest(Person):
    def __init__(self, name, city, status):
        Person.__init__(self, name, city)
        self.status = status

    def tell(self):
        Person.tell(self)
        print(' Статус: "{0}"»'.format(self.status))

t = Guest('Иван Петров', 'Москва', 'Наставник')
s = Guest('Степанов Степанов', 'Пермь', 'Волонтер')

members = [t, s]
for member in members:
    member.tell()
