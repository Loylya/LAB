# ЛАБА_4
# ЗАДАНИЕ_1

# cislo = int(input("введите число"))
# if cislo % 3 == 0:
#     print ("делится на 3")
# else:
#     print ("не делится на 3")

# # ЗАДАНИЕ_2

# try:
#     chislo_vvod = input("введите число: ")
#     chislo = float(chislo_vvod)
#     itog = 100 / chislo
#     print (f"результат: {itog}")
#
# except ZeroDivisionError:\
#         print("Ошибка деления на ноль.")
# except ValueError:\
#         print("Невозможно преобразовать строку в число.")


# # ЗАДАНИЕ_3

# def magic(data_chislo):
#     try:
#         den, mec, god = map(int, data_chislo.split("."))
#         posl = god % 100
#
#         if den * mec== posl:
#             return True
#         else:
#             return False
#     except(ValueError, IndexError):
#         return False
#
# data_chislo_vvod = input("введите дату (ДД.ММ.ГГГГ):")
#
# if magic(data_chislo_vvod):
#     print("Это магическая дата")
# else:
#     print("Это НЕ магическая дата")


# ЗАДАНИЕ_4

# def magic_bilet(bilett):
#     if len(bilett) % 2 != 0:
#         return False
#
#     polovinki = len(bilett) // 2
#     polovinka_1 = bilett[:polovinki]
#     polovinka_2 = bilett[polovinki:2*polovinki]
#
#     sum_1_polov = 0
#     for chch in polovinka_1:
#         sum_1_polov = sum_1_polov + int(chch)
#
#     sum_2_polov = 0
#     for chch in polovinka_2:
#         sum_2_polov = sum_2_polov + int(chch)
#
#     if sum_1_polov == sum_2_polov:
#         return True
#     else:
#         return False
#
# r = input("Введите четное число: ")
#
# if magic_bilet(r):
#     print ("Это счастливый билет!")
# else:
#     print("Это обычный билет(")






