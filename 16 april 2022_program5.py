angka_awal = 1
jarak_permulaan = 1
baris = 7
 
for i in range(baris):
    for column in range(1, jarak_permulaan+1):
        print(angka_awal, end=' ')
        angka_awal += 1
    print("")
    jarak_permulaan += 1
