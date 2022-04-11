tahun = int(input('masukan tahun : '))

if (tahun % 400 == 0) :
    print("tahun kabisat")
elif(tahun % 100 == 0) :
    print('tahun kabisat')
else:
    print("bukan tahun kabisat")
