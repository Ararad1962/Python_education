#управляющие символы в строках
print("Привет\nПривет\nПривет")
print("""Привет!
Привет!
Привет!""")
print("Привет\tПривет\tПривет")
print('"Текст в кавычках"')
print("'Текст в опострофах'")
print("Буква \"В\" в кавычках")

#Операции со строками
text= "Привет"
text1 = "мир"
print (text+' '+text1)
print (text*5)
print (text[0])
print (text[0:3])
print (text[-1])

# Методы
print (text.upper())
print (text.lower())
print (text.capitalize())

text2="Привет мир куда идешь"
print (text2.split(" ")) # создание списка из строки

spisok = ["a", "b","c"]
print (", ".join(spisok)) # создание строки из списка

text3 = "    alkhfjakls sdnfjvnty      "
print (text3.strip()) # удаление лишних пробелов
print (text3.lstrip()) # удаление лишних пробелов вначале строки
print (text3.rstrip()) # удаление лишних пробелов вконце строки

text4="ioioioio"
print (text4.replace("i", "L")) # замена букв i на L