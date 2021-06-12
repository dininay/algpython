# Dini Naylul Izzah - 20083000059 - 2b
# Cek Kelulusan Soal 7c Aplikasi 5 
pil = "y"
while pil == "y" or pil == "Y":

    print ("===================================================")
    print ("Tampilkan Nilai Huruf dengan Inputan Bilangan Bulat")
    print ("===================================================")

    b = input(">> Masukkan Bilangan Bulat = ")

    if int (b)>80 and int (b)<=100 :
        sts ="Baik Sekali"
    elif int(b)>=65: 
        sts ="Baik"
    elif int(b)>=55: 
        sts ="Cukup"
    elif int(b)>=40: 
        sts ="Kurang"
    elif int(b)>=0:
        sts = "Kurang Sekali"
    else :
        sts = ">>> Masukkan Bilangan Bulat 0-100 Saja"
    print (sts)

    pil = input(">> Mulai Ulang Program? y/t = ")
    if pil == "t" or pil == "T" :
        break