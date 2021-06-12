# Dini Naylul Izzah - 20083000059 - 2b
# Cek Kelulusan Soal 7a Aplikasi 5 
pil = "y"
while pil == "y" or pil == "Y":
    print ("=============")
    print ("Cek Kelulusan")
    print ("=============")

    n = input(">> Masukkan Nilai = ")

    if int (n)>60 and int (n)<=100:
        sts = "Lulus"
    else :
        sts = "Ulang"

    print (sts)

    pil = input(">> Mulai Ulang Program? y/t = ")
    if pil == "t" or pil == "T" :
        break