# # ЗДАЧА_1
#
# from PIL import Image
# import os
#
# # Путь к папке с исходными изображениями
# folder_path = "/Users/olgakristal/PycharmProjects/LABA_9/CH"
#
# # Создаем папку для обработанных изображений
# processed_folder_path = "/Users/olgakristal/PycharmProjects/LABA_9/processed_images"
# os.makedirs(processed_folder_path, exist_ok=True)
#
# # Цикл по всем изображениям в папке
# for filename in os.listdir(folder_path):
#     if filename.endswith(".jpg") or filename.endswith(".png"):
#         # Открываем изображение
#         image_path = os.path.join(folder_path, filename)
#         image = Image.open(image_path)
#
#         # Некоторая обработка изображения, например, изменение размера
#         new_size = (image.size[0] // 2, image.size[1] // 2)
#         image = image.resize(new_size)
#
#         # Сохраняем обработанное изображение в новом каталоге
#         processed_filepath = os.path.join(processed_folder_path, filename)
#         image.save(processed_filepath)
#         print(f"Сохранено обработанное изображение: {filename}")



# # ЗАДАЧА_3
#
# import csv
#
# total_cost = 0
#
# # Открываем файл с данными
# with open('//Users/olgakristal/PycharmProjects/LABA_9/PRODUKTI.csv', 'r') as file:
#     # Создаем объект для чтения данных из файла
#     csv_reader = csv.reader(file)
#     # Пропускаем заголовок
#     next(csv_reader)
#
#     print("Нужно купить:")
#
#     # Цикл по строкам в файле
#     for row in csv_reader:
#         product, quantity, price = row
#         cost = int(quantity) * int(price)
#         total_cost += cost
#         print(f"{product} - {quantity} шт. за {price} руб.")
#
#     print(f"Итоговая сумма: {total_cost} руб.")