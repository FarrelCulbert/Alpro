nama = input('Nama \t\t: ')
nim = input('NIM \t\t: ')
program_studi = input('Program Studi \t: ')
mata_kuliah = input('Mata Kuliah \t: ')

def fungsi_nilai(nilai_ujian):
    nilai_ujian = int(nilai_ujian)
    return nilai_ujian


def fungsi_percabangan(var_nilai):
    var_indeks = ""
    if(var_nilai > 0 and var_nilai <= 40):
        var_indeks = "E"
    elif(var_nilai > 40 and var_nilai <= 55) :
        var_indeks = "D"
    elif(var_nilai > 55 and var_nilai <= 60) :
        var_indeks = "C"
    elif(var_nilai > 60 and var_nilai <= 65) :
        var_indeks = "BC"
    elif(var_nilai > 65 and var_nilai <= 70) :
        var_indeks = "B"
    elif(var_nilai > 70 and var_nilai <= 80) :
        var_indeks = "AB"
    elif(var_nilai > 80 and var_nilai <= 100) :
        var_indeks = "A"
    return var_indeks

def fungsi_input ():
    var_fungsi_input = 0
    var_nilai_ujian = input('Nilai Ujian \t: ')
    var_fungsi_input += (int(fungsi_nilai(var_nilai_ujian)))
    return var_fungsi_input

var_total = fungsi_input()


#Output
print('======Nilai Mata Kuliah======')
print('Predikat Nilai : ', fungsi_percabangan(var_total))

if (fungsi_percabangan(var_total) == "A"):
    print('Selamat anda lulus mata kuliah',mata_kuliah)
elif(fungsi_percabangan(var_total) == "AB"):
    print('Selamat anda lulus mata kuliah',mata_kuliah)
elif(fungsi_percabangan(var_total) == "B"):
    print('Selamat anda lulus mata kuliah',mata_kuliah)
elif(fungsi_percabangan(var_total) == "BC"):
    print('Anda tidak lulus mata kuliah',mata_kuliah)
elif(fungsi_percabangan(var_total) == "C"):
    print('Anda tidak lulus mata kuliah',mata_kuliah)
elif(fungsi_percabangan(var_total) == "D"):
   print('Anda tidak lulus mata kuliah',mata_kuliah)
elif(fungsi_percabangan(var_total) == "E"):
    print('Anda tidak lulus mata kuliah',mata_kuliah)

print('=============================')

#2 April 2022 @Algoritma dan Pemograman

