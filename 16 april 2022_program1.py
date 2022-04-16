# #menggunakan input
# awal= int(input('masukan angka awal : '))
# akhir= int(input('masukan angka akhir : '))
# z=[]
# x=[]
# y=[]
# for i in range(awal,akhir+1):
#     if i :
#        z.append(i)
#     if i%2 == 0 :
#        x.append(i)
#     if i%2 == 1:
#        y.append(i)
# print(z)
# print("bilangan genap :",x)
# print("banyak bilangan genap :",len(x))
# print("bilangan ganjil : ",y)
# print("banyak bilangan ganjil :",len(y))

#tanpa input
nilai= [10, 5, 1, 4, 9]
c=[]
x=[]
y=[]
for i in nilai:
    if i :
        c.append(i)
    if i%2 == 0 :
        x.append(i)
    if i%2 == 1:
        y.append(i)
print('list angka :',c)
print("bilangan genap :",x)
print("banyak bilangan genap :",len(x))
print("bilangan ganjil : ",y)
print("banyak bilangan ganjil :",len(y))
