#Работа со словарями
dict= {"яблоко": "красное", "банан":"желтый","лимон":"желтый"}
print(dict)
for k in dict.keys():
   print(k)
for k in dict.values():
   print(k)
for k in dict.items():
   print(k)

print (dict ['банан'])

dict ['банан']= "зеленый"
print (dict)

del(dict["банан"])
print (dict)