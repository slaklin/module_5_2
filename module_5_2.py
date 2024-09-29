class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if self.number_of_floors < new_floor or new_floor < 1:
            print("Такого этажа не существует")
        else:
            new_floor += 1
            for i in range(1, new_floor):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('ЖК Горский', 12)
h2 = House('Домик в деревне', 3)

print(h1)
print(h2)
print(len(h1))
print(len(h2))
# h1.go_to(9)
# h2.go_to(4)