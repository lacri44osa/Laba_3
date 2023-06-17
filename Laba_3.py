class Earth:
    def __init__(self, animal, animal_2):
        self.animal = animal
        self.animal_2 = animal_2

    def rabbit(self):
        print("Rabbit on Earth")

    def wolf(self):
        print("Wolf on Earth")

    def turtle(self):
        print("Fox on Earth")


class Water(Earth):
    def __init__(self, animal, animal_2, animal_3):
        super().__init__(animal, animal_2)
        self.animal_3 = animal_3

    def turtle(self):
        print("Turtle in Water")


class Air(Earth):
    def __init__(self, animal="default_animal", animal_2="default_animal_2"):
        super().__init__(animal, animal_2)

    def eagle(self):
        print("Eagle in Air")

    def pigeon(self):
        print("Pigeon in Air")


a = Earth('animal_value', 'animal_2_value')
b = Water('animal_value', 'animal_2_value', 'animal_3_value')
c = Air()

a.rabbit()
a.wolf()
a.turtle()

b.rabbit()
b.wolf()
b.turtle()

b.rabbit()
b.wolf()
b.turtle()
c.eagle()
c.pigeon()

