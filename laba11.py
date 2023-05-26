def zadacha1():
    print("Задача 1: ")
    class Restaurant:
        def __init__(self,restaurant_name,cuisine_type):     #init -присваеваем атрибутам значения переданные при создании экземпляра класс
            self.restaurant_name = restaurant_name      #sellf - параметр, который передаётся первым аргументом в метод класса и представляет собой ссылку на экземпляр класса
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):      #метод1 выводит информацию о ресторане используя атрибуты
            print("Название ресторана: ",self.restaurant_name ,"\nКухня ресторана: ",self.cuisine_type)
        def open_restaurant(self):      #метод2 выводит сообщение о том что ресторан открыт
            print("Ресторан открыт к посещению!")
    newRestaurant = Restaurant("Грюза","Грузинская") #создаем экземпляр класа
    newRestaurant.describe_restaurant() #выводит значене по отдельности
    newRestaurant.open_restaurant() # вызывает оба метода


def zadacha2():
    print("Задача 2: ")
    class Restaurant:
        def __init__(self,restaurant_name,cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print("Название ресторана: ",self.restaurant_name ,"\nКухня ресторана: ",self.cuisine_type)
        def open_restaurant(self):
            print("Ресторан открыт к посещению!")
    newRestaurant = Restaurant(input("Введите название ресторана: "),input("Какая это будет кухня? "))
    secondRestaurant=Restaurant("Грюза","Грузинская")
    thirdRestaurant=Restaurant("Матрешка","Русская")

    newRestaurant.describe_restaurant()
    secondRestaurant.describe_restaurant()
    thirdRestaurant.describe_restaurant()



def zadacha3():
    print("Задача 3: ")
    class Restaurant:
        def __init__(self, name, cuisine_type, initial_rating):
            self.name = name
            self.cuisine_type = cuisine_type
            self.rating = initial_rating

        def describe_restaurant(self):
            print(f"{self.name} ресторан с {self.cuisine_type} кухней, рейтинг которого {self.rating}.")

        def update_cuisine_type(self,new_cuisine_type ):
            self.cuisine_type = new_cuisine_type
    restaurant1 = Restaurant(" France", "Французская", 4.7)
    restaurant1.describe_restaurant()

    restaurant1.update_cuisine_type("Итальянская")
    restaurant1.describe_restaurant()

zadacha1(), zadacha2(), zadacha3()







