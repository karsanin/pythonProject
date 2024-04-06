import os
# import requests
#
# response = requests.get('https://greenwayglobal.com/shop/?country=RU&dc=1&lang=ru')
# # print(response.ok)  # проверяем успешен ли запрос?
# # print(response.text)  # выводим полученный ответ на экран
#
# import pandas as pd
#
# print(pd.read_csv('text2.txt', sep='.')) # delimiter='/',
#
# import numpy as np
#
# a = np.zeros((3, 5))
# print(a)
# b = np.ones((3, 5))
# print(b)
# c = a + b*2
# print(c)

import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
# plt.show()

# fruits = ["apple", "peach", "orange", "bannana", "melon"]
# counts = [34, 25, 43, 31, 17]
# plt.bar(fruits, counts)
# plt.title("Fruits!")
# plt.xlabel("Fruit")
# plt.ylabel("Count")
# plt.show()

from PIL import Image
from PIL import ImageFilter

original = Image.open("222.png")


print("Размер изображения:")
print(original.format, original.size, original.mode)

# размываем изображение
blurred = original.filter(ImageFilter.BLUR)
# открываем оригинал и размытое изображение
original.show()
blurred.show()
# сохраняем изображение
blurred.save("blurred.png")
