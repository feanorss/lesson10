class Person:
    def __init__(self, name, age, gender, occupation,farbaoci):
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

class Student(Person):
    def __init__(self, name, age, gender, occupation, farbaoci, score):
        super().__init__(name, age, gender, occupation, farbaoci)
        self.score = score

    def jeGenius(self):
        if self.score > 90:
            print(f"{self.name} je genius a {self.gender}")
        else:
            print(f"{self.name} nie je genius a {self.gender}")


patrik = Student("Patrik", 30, "muz", "Kysuce","cierna", 95)
patrik.pozdrav()
patrik.bydlisko()
milos = Student("Milos", 33, "muz", "Bratislava", "zelena", 48)
milos.pozdrav()
milos.bydlisko()
milos.zostarni(30)
print(milos.farbaoci)

