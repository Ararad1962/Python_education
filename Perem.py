a=45
b=5
def f():
   global a
   global b
   a=a+b
   print(a)



f()
print (a)
