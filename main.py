class Person:
    def __init__(self, name, age, gender, occupation, farbaoci):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.farbaoci = farbaoci

    def pozdrav(self):
        print(f"Ahoj volam sa {self.name} a mam {self.age} rokov")

    def bydlisko(self):
        print(f"Ahoj volam sa {self.name} ,byvam v meste {self.occupation}")

    def zostarni(self, pocetrokov):
        vek = self.age - pocetrokov
        print(f"zostarol som na {vek}")


patrik = Person("Patrik", 30, "muz", "Kysuce","cierna")
patrik.pozdrav()
patrik.bydlisko()
milos = Person("Milos", 33, "muz", "Bratislava", "zelena")
milos.pozdrav()
milos.bydlisko()
milos.zostarni(30)
print(milos.farbaoci)

