#Открытие (Создание) и запись в файл
f = open("1.txt", "w")
f.write("Привет, файл!")
f.close()

#Чтение из файла
f = open("1.txt", "r")
print(f.read())
f.close()

#Открытие, добавление записи и чтение файла без метода Close
with open("1.txt", "a") as a:
   a.write("бугага")
with open("1.txt", "r") as r:
   print(r.read())

#Обработка Исключения Деления на ноль
try:
   x = int(input())
   y = int(input())
   print(x/y)
except ZeroDivisionError:
   print("На ноль делит нельзя!")

