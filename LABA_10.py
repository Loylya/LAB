# # ЗАДАНИЕ_1
#
# import json
#
# def jsn():
#     filename = 'Proba.json'
#     with open(filename, 'r', encoding='utf-8') as file:
#         data = json.load(file)
#
#         for product in data['products']:
#             print(f"Название: {product['name']} Цена: {product['price']}")
#             print(f"Вес: {product['weight']}")
#             if product['available']:
#                 print("В наличии")
#             else:
#                 print("Нет в наличии!")
#             print()


# # ЗАДАНИЕ_2
#
# import json
# import os
#
# filename = '/Users/olgakristal/PycharmProjects/LABA_10/Proba_1.json'
#
# def add_product_to_file(product):
#     if not os.path.exists(filename):
#         with open(filename, 'w', encoding='utf-8') as file:
#             json.dump({"products": []}, file, ensure_ascii=False)
#
#     with open(filename, 'r', encoding='utf-8') as file:
#         data = json.load(file)
#         data['products'].append(product)
#
#     with open(filename, 'w', encoding='utf-8') as file:
#         json.dump(data, file, ensure_ascii=False, indent=4)
#
# while True:
#     name = input("Введите название продукта: ")
#     price = int(input("Введите цену продукта: "))
#     weight = int(input("Введите вес продукта: "))
#     available = input("Продукт в наличии? (да/нет): ").lower() == 'да'
#
#     product = {
#         "name": name,
#         "price": price,
#         "weight": weight,
#         "available": available
#     }
#
#     add_product_to_file(product)
#
#     add_more = input("Хотите добавить еще продукт? (да/нет): ").lower()
#     if add_more != 'да':
#         break







# # Открываем файл с англо-русским словарем для чтения
# with open('en-ru.txt', 'r') as file:
#     lines = file.readlines()
#
# # Создаем словарь для хранения русско-английского словаря
# ru_en_dict = {}
#
# # Обрабатываем строки из файла и создаем русско-английский словарь
# for line in lines:
#     pairs = line.strip().split(' - ')
#     if len(pairs) == 2:
#         eng_word, ru_translations = pairs[0], pairs[1].split(',')
#         for ru_word in ru_translations:
#             ru_word = ru_word.strip()
#             if ru_word in ru_en_dict:
#                 ru_en_dict[ru_word].append(eng_word)
#             else:
#                 ru_en_dict[ru_word] = [eng_word]
#
# # Записываем русско-английский словарь в файл ru-en.txt
# with open('ru-en.txt', 'w') as output_file:
#     for ru_word, eng_translations in ru_en_dict.items():
#         output_file.write(f"{ru_word} – {', '.join(eng_translations)}\n")



# # ЗАДАЧА_3
#
# def create_ru_en_dictionary(input_file, output_file):
#     ru_en_dict = {}
#     with open(input_file, 'r') as file:
#         for line in file:
#             words = line.strip().split(' - ')
#             if len(words) == 2:
#                 en_word = words[0].strip()
#                 ru_translations = [ru.strip() for ru in words[1].split(',')]
#                 for ru_word in ru_translations:
#                     ru_en_dict[ru_word] = en_word
#
#     sorted_ru_en_list = sorted(ru_en_dict.items())
#
#     with open(output_file, 'a') as outfile:
#         for ru_word, en_word in sorted_ru_en_list:
#             outfile.write(f"{ru_word} – {en_word}\n")
#
# input_file = 'Proba.txt'
# output_file = 'ru-en.txt'
#
# create_ru_en_dictionary(input_file, output_file)




