# Dini Naylul Izzah - 20083000059 - 2b
# Cek Kelulusan Soal 8b Aplikasi 6
pil = "y"
while pil == "y" or pil == "Y":

    print ("==========================================")
    print ("Total Transaksi Pembelian Printer + Diskon")
    print ("==========================================")

    print ("Berikut Daftar Harga Produk")
    print ("Printer Epson T20 : Rp.660000")

    p = int(input(">> Masukkan Jumlah Pembelian Printer = "))
    h = 660000

    total = p * h
    diskon = 0.15 / 100

    if int(total)>=660000 and int(total)<1500000 : 
        print ("Total Harga : Rp." , total)
    elif int(total)>=1500000 : 
        print ("Total Harga : Rp." , total - diskon)
    else :
        print ("Jumlah tidak boleh 0")

    pil = input(">> Mulai Ulang Program? y/t = ")
    if pil == "t" or pil == "T" :
        break