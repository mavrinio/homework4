#1 задание 
class Car:
    def __init__(self, brand, color, fuel):
         self.brand = brand
         self.color = color
         self.fuel = fuel
        
    def __str__(self):
        return f'Брэнд авто - {self.brand}  цвет кузова : {self.color} тип пожираемого топлива: {self.fuel}'

g = Car ('Toyota','черный.','дизель')
print(g)
#2 задание 
class Monkey: 
    max_age = 12 
    loves_bananas = True #наследование
 
    def climb(self): 
     print('Я ЗАБИРАЮСЬ НА ДЕРЕВО ')  
    
    # def __str__(self): 
    #     return f'столько лет {chichi.max_age} , и любят ли бананы ? {chichi.loves_bananas} {chichi.climb} '

chichi= Monkey() 
fichi = Monkey() 
print(f'столько лет : {chichi.max_age} , и любят ли бананы ? {chichi.loves_bananas}') 
chichi.climb() 
 
print(f'столько лет : {fichi.max_age} , и любят ли бананы ? {fichi.loves_bananas}') 
fichi.climb()
 
 
#3 задание 

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age 
        self.gender = gender
    
    def calculate_age(self, past):
        self.past = past
    
    def __str__(self):
        return f'Через {self.past} года , {self.name} будет {self.age + self.past } лет'

human = Person('ИГАРю', 33,'male')
# print(human)
human.calculate_age(4)
print(human)