# Dini Naylul Izzah - 20083000059 - 2b
# Cek Golongan Usia Soal 7b Aplikasi 5 
pil = "y"
while pil == "y" or pil == "Y":

    print ("=================")
    print ("Cek Golongan Usia")
    print ("=================")

    u = input(">> Masukkan Usia = ")

    if int (u)>60 and int (u)<=100 :
        sts ="Lansia"
    elif int(u)>=35: 
        sts ="Dewasa"
    elif int(u)>=18: 
        sts ="Pemuda"   
    elif int(u)>=15: 
        sts ="Remaja"
    elif int(u)>=0:
        sts = "Anak"
    else :
        sts = ">>> Masukkan Angka Usia 0-100 Saja"
    print (sts)

    pil = input(">> Mulai Ulang Program? y/t = ")
    if pil == "t" or pil == "T" :
        break