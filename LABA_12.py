class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restuarant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        description = f"русторан '{self.restuarant_name}' кухня '{self.cuisine_type}'"
        return description


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, location, working_hours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.working_hours = working_hours

    def display_flavors(self):
        print("Список сортов мороженого:")
        for flavor in self.flavors:
            print(flavor)

    def add_flavor(self, new_flavor):
        self.flavors.append(new_flavor)
        print(f"Сорт мороженого '{new_flavor}' был добавлен")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Сорт мороженого '{flavor}' был удален")
        else:
            print(f"Сорт мороженого '{flavor}' не найден")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Сорт мороженого '{flavor}' доступен")
        else:
            print(f"Сорт мороженого '{flavor}' не доступен")


# Создаем экземпляр класса IceCreamStand
ice_cream_stand = IceCreamStand("Кафе-мороженое 'Сластена'", "мороженое",
                                ["ванильное", "шоколадное", "клубничное"],
                                "ул. Летняя, д. 10", "с 10:00 до 22:00")

# Выводим информацию о кафе-мороженом
print(ice_cream_stand.describe_restaurant())
print(f"Локация: {ice_cream_stand.location}")
print(f"Время работы: {ice_cream_stand.working_hours}")

# Выводим список сортов мороженого
ice_cream_stand.display_flavors()

# Добавляем новый сорт мороженого
ice_cream_stand.add_flavor("банановый")
ice_cream_stand.display_flavors()

# Удаляем существующий сорт мороженого
ice_cream_stand.remove_flavor("клубничное")
ice_cream_stand.display_flavors()

# Проверяем доступность определенного сорта мороженого
ice_cream_stand.check_flavor("шоколадное")
ice_cream_stand.check_flavor("клубничное")
