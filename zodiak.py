day = int(input("masukan tanggal : "))
month = input('masukan bulan : ')

if month == 'april' :
    zodiak = 'aries' if (day <20) else ('taurus')

elif month == 'mei' :
    zodiak = 'taurus' if (day <21 ) else  ('gemini')

elif month == 'juni' :
    zodiak = 'gemini' if (day <21 ) else  ('kanser')

elif month == 'juli' :
    zodiak = 'kanser' if (day <23 ) else  ('leo')

elif month == 'agustus' :
    zodiak = 'leo' if (day <23 ) else  ('virgo')

elif month == 'september' :
    zodiak = 'virgo' if (day <23 ) else  ('libra')
    
elif month == 'oktober' :
    zodiak = 'libra' if (day <23 ) else  ('skorpio')

elif month == 'november' :
    zodiak = 'skorpio' if (day <23 ) else  ('sagitarius')

elif month == 'desember' :
    zodiak = 'sagitarius' if (day <22 ) else  ('kaprikon')

elif month == 'januari' :
    zodiak = 'kaprikon' if (day <20 ) else  ('akuarius')

elif month == 'februari' :
    zodiak = 'akuarius' if (day <19 ) else  ('pisces')

elif month == 'maret' :
    zodiak = 'pisces' if (day <21 ) else  ('aries')
    
print (zodiak)