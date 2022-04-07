#percabangan dalam kehidupan sehari-hari

#sortir barang berdasarkan berat untuk memilih kendaraan yang akan digunakan
berat = float(input('masukan berat barang (dalam kg): '))

if (berat > 30) :
    print("kirim barang menggunakan mobil")
elif(berat >10 and berat <= 30) :
    print("kirim barang mengagunakan motor")
else:
    print("kirim barang menggunakan sepeda")

