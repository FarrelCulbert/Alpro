a = int(input('masukan nilai a : '))
b = int(input('masukan nilai b : '))
c = int(input('masukan nilai c : '))

if a==b==c :
    print('segitiga sama sisi')
elif a==b or b==c or c==a :
    print('segitiga sama kaki')
else :
    print('segitiga sembarang')