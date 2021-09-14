#Работа со списками

spisok = []
numbers = [3,4,5,9,10]
print (numbers)

numbers = [3,5,34,1,'name']
print(numbers)

numbers = [3,5,3,1, [45,7]]
print(numbers)

names = ['Кеша', 'Толик', 'Попугай']
print (names [1])

print (names [-1])

for name in names:
   print (name)
print(names)

names.append('Попугай1')
print(names)

names.pop()
print(names)

n= names.index ('Толик')
print(n)

print(len(names))

list = [4,6,81,95,108,56]

list.sort (reverse=True)
print(list)

list[1]='b'
print(list)

letters=['asdafs','aefefcasd','jhgfjt']
letters.sort()
print (letters)