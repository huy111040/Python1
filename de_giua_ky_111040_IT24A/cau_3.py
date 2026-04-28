from abc import ABC, abstractmethod

class Person(ABC):
    count = 0

    def __init__(self, name ="", age = 0):
        self.__name = name
        self.__age = age
        Person.count += 1

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    @abstractmethod
    def introduce(self):
        pass

class Doctor(Person):
    count_doc = 0

    def __init__(self, name="", age=0):
        super().__init__(name, age)
        Doctor.count_doc += 1

    def introduce(self):
        print(f"Hello, my name is {self.get_name()}. I am {self.get_age()} years old. I am a Doctor.")

    def __str__(self):
        return f"Lớp cha: Person, số đối tượng Doctor được tạo ra: {Doctor.count_doc} , tổng số đối tượng Person: {Person.count}"

class Patient(Person):
    count_pat = 0

    def __init__(self, name, age):
        super().__init__(name, age)
        Patient.count_pat += 1   # đếm riêng patient

    def introduce(self):
        print(f"Hello, my name is {self.get_name()}. I am {self.get_age()} years old. I am a Patient.")

    def __str__(self):
        return f"Lớp cha: Person , số đối tượng Patient được tạo ra: {Patient.count_pat} , tổng số đối tượng Person: {Person.count}"



if __name__ == "__main__":

    people = []

    d1 = Doctor("Hải", 40)
    d2 = Doctor("Hương", 35)
    p1 = Patient("Bảo", 20)
    p2 = Patient("Tâm", 25)

    people.extend([d1, d2, p1, p2])

    for person in people:
        person.introduce()
        print(person)
