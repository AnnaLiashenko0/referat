Порушується:
class Bird:
    def fly(self):
        print("Flying")

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches cannot fly!")

# Викликаємо метод fly для об'єкта Ostrich
bird = Ostrich()
bird.fly()  # Порушення принципу підстановки Лісков








Приклад застосування в Python:
class Bird:
    def fly(self):
        print("Flying")

class Eagle(Bird):
    def fly(self):
        print("Eagle flying high")

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly")

def make_bird_fly(bird: Bird):
    bird.fly()
