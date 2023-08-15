#Клас це відносне креслення обьекта(це шаблон для створення обьекта)
#обьект классу називають екземпляром классу
# кожен класс може мати в собі основні атрибути та методи


class Car:
    name = "Nisan"
    model = "Skyline GT-R-R34"
    year = 2000
    def start_engine(self):
        print("Двигун почав працювати: ")
    def off_engine(self):
        print("Двигун завершив працю: ")
    def on_lights(self):
        print("Фари почали працювати: ")
    def off_lights(self):
        print("Фари завершили працю: ")
    def turn_left(self):
        print("Колеса повернулись на ліво: ")
    def turn_right(self):
        print("Колеса повернулись на право:")
    
car1 = Car()
car2 = Car()
print(type(car1))
print(car1.year)
print(car2.year)
car1.year = 1875
print(car1.year)
print(car2.start_engine())