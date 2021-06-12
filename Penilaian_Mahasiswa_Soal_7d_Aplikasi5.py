# Dini Naylul Izzah - 20083000059 - 2b
# Cek Kelulusan Soal 7d Aplikasi 5 
pil = "y"
while pil == "y" or pil == "Y":

    print ("===================================================")
    print ("Peniilaian Mahasiswa mendapat Nilai X dengan Syarat")
    print ("===================================================")

    x = input(">> Masukkan Nilai Mahasiwa = ")

    if int (x)>=91 and int (x)<=100 :
        sts ="A"
    elif int(x)>=81: 
        sts ="B"
    elif int(x)>=71: 
        sts ="C"
    else :
        sts = "D"
    print (sts)

    pil = input(">> Mulai Ulang Program? y/t = ")
    if pil == "t" or pil == "T" :
        break