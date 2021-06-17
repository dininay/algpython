# Dini Naylul Izzah - 20083000059 - 2b
# Transaksi Biaya Ekspedisi Quiz 2 Soal 2
pil = "y"
while pil == "y" or pil == "Y":

    print ("=============================================")
    print(" BENGKEL MOTOR UD.MATAHARI ")
    print ("=============================================")
    print("Daftar Harga Oli Motor")
    print(" A. Duration SW20 1L         = Rp. 53.000")
    print(" B. Castrol Magnatec 1L      = Rp. 50.000")
    print(" C. Federal Supreme XX 1L    = Rp. 54.000")
    print(" D. Yamalube 1L              = Rp. 45.000")
    print(" E. Shell 1L                 = Rp. 46.000")
    
    print ("=============================================")

    kode =['a','b','c','d','e']

    merk = ['Duration SW20 1L','Castrol Magnatec 1L','Federal Supreme XX 1L','Yamalube 1L','Shell 1L']
    harga = [53000,50000,54000,45000,46000]

    pilihan = input(">> Masukkan Kode Oli = ")
    qty = int(input(">> Masukkan Jumlah Pembelian = "))
    print(">>>-------------------------------------")
    #identifikasi pilihan
    if pilihan=="a" or pilihan=="A":
        idx = 0
    elif pilihan=="b" or pilihan=="B":
        idx = 1
    elif pilihan=="c" or pilihan=="C":
        idx = 2
    elif pilihan=="d" or pilihan=="D":
        idx = 3
    elif pilihan=="e" or pilihan=="E":
        idx = 4
    else:
        idx = 0

    #cetak tampilan layar
    print(">>> Pesanan        = " + merk[idx])
    print(">>> Harga          = Rp." + str(harga[idx]))
    print(">>> Jumlah Pesanan = ",qty)

    #hitung transaksi

    fixharga = harga[idx]
    fixqty = qty
    total = fixharga * fixqty
    ppn = total * 0.01

    if total <200000 :
            diskon = (0)
            totalakhir = total + ppn
    else :
            diskon = total*0.05
            totalakhir = total-diskon+ppn

    #tampilkan total akhir
    print(">>>-------------------------------------")
    print(">>> Total           = Rp." + str(total))
    print(">>> Diskon          = Rp." + str(diskon))
    print(">>> PPN             = Rp." + str(ppn))
    print(">>>-------------------------------------")
    print(">>> Total Akhir     = Rp." + str(totalakhir))

    pil = input(">> Membuat Transaksi Lain? y/t = ")
    if pil == "t" or pil == "T" :
        break