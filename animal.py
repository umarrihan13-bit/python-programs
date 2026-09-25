from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name,habitat):
        self.name = name
        self.habitat = habitat

        def display(self):
            print(f"Name: {self.name} | Habitat: {self.habitat}")

            @abstractmethod
            def speak(self):
                pass

            class Dog(Animal):

                def __init__(self, name, habitat, breed):
                    super().__init__(name, habitat)
                    self.breed = breed

                def speak(self):
                    print(f"{self.name} ({self.breed})" says: Woof!")


    class parrot(Animal):

        def __init__(self, name, habitat, phrase):
            super().__init__(name, habitat)
             self.phrase = phrase
                def speak(self):
             print(f"{self.name} says: {self.phrase}")

class lion(Animal):

    def __init__(self, name, habitat, pride):
    super().__init__(name, habitat)
    self.pride = pride

    def speak(self):
        print(f"{self.name} (Pride: {self.pride}) says: Roar!")

dog = Dog("Brunno","home","labrador")
parrot = parrot("Polly","forest","Hello!")
lion = lion("Simba","savannah","Pride Rock")

print("=== Animal sound show ===\n")
for animal in [dog, parrot, lion]:
    animal.display()
    animal.speak()
    print()
        
            
