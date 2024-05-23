# (СДАНО)

# Задание «Ресторан»:
# ЗАДАЧА_1
#
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restuarant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         description = f"русторан '{self.restuarant_name}' кухня '{self.cuisine_type}'"
#         return description
#
#     def open_restaurant(self):
#         return f"лучший ресторан города '{self.restuarant_name}' открылся. вас ждет восхитительная {self.cuisine_type} кухня"
#
# restaurant_1 = Restaurant("уютное кафееееЭЭэЭе с плетенной мебелью на ууулице", "грузинская")
#
# restaurant_description = restaurant_1.describe_restaurant()
# print(restaurant_description)
#
# restaurant_open_message = restaurant_1.open_restaurant()
# print(restaurant_open_message)


# # ЗАДАНИЕ_2
#
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restuarant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         description = f"русторан '{self.restuarant_name}' кухня '{self.cuisine_type}'"
#         return description
#
# restaurant_1 = Restaurant("уютное кафееееЭЭэЭе с плетенной мебелью на ууулице", "грузинская")
# restaurant_2 = Restaurant("жареные гвозди", "итальянская")
# restaurant_3 = Restaurant("звезда удачи", "мексиканская")
#
# print(restaurant_1.describe_restaurant())
# print(restaurant_2.describe_restaurant())
# print(restaurant_3.describe_restaurant())


# # ЗАДАЧА_3
#
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type, rating = 0):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.rating = rating
#
#     def describe_restaurant(self):
#         description = f"ресторан '{self.restaurant_name}' кухня '{self.cuisine_type}' рейтинг '{self.rating}'"
#         return description
#
#     def update_rating(self, new_rating):
#         self.rating = new_rating
#         return f"Рейтинг ресторана '{self.restaurant_name}' рейтинг обновлен: {self.rating}"
# restaurant_1 = Restaurant("кафе 'жареные гвозди'", "итальянская", 3.4)
# print(restaurant_1.describe_restaurant())
#
# new_rating = 4.9
# update_message = restaurant_1.update_rating(new_rating)
# print(update_message)
