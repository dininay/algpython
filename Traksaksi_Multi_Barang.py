# Dini Naylul Izzah - 20083000059 - 2b
# Tugas - Latihan Multi Barang Per Transaksi
pil = "y"
while pil == "y" or pil == "Y":

    print ("=============================================")
    print(" KANTIN FAKULTAS TEKNOLOGI INFORMASI ")
    print ("=============================================")
    print("Menu Makanan")
    print(" A. Nasi Goreng              = Rp. 15.000")
    print(" B. Lontong Goreng           = Rp. 14.900")
    print(" C. Bakso Goreng             = Rp. 12.900")
    print(" D. Rujak Goreng             = Rp. 13.000")
    print(" E. Rujak Bakso              = Rp. 15.000")
    print(" F. Rujak Bakso Pecel        = Rp. 17.000")
    
    print ("=============================================")

    print("Menu Minuman")
    print(" AA. Teh Dingin/Hangat/Panas  = Rp. 2.500")
    print(" BB. Kopi Dingin              = Rp. 5.000")
    print(" CC. Kopi Teh Panas           = Rp. 6.500")
    print(" DD. Coca Cola Dingin         = Rp. 3.500")
    print(" EE. Coca Cola Panas          = Rp. 5.000")
    
    print ("=============================================")

    nama = ""
    total = 0

    kode=['a','b','c','d','e','f','aa','bb','cc','dd','ee']

    menu = ['Nasi Goreng','Lontong Goreng','Bakso Goreng','Rujak Goreng','Rujak Bakso','Rujak Bakso Pecel','Teh Dingin/Hangat/Panas','Kopi Dingin','Kopi Teh Panas','Coca Cola Dingin','Coca Cola Panas']
    harga = [15000,14900,12900,13000,15000,17000,2500,5000,6500,3500,5000]

    pilihan = input(">> Kode Pesanan            = ")
    qty = int(input(">> Jumlah Pembelian        = "))

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
    elif pilihan=="f" or pilihan=="F":
        idx = 5
    elif pilihan=="aa" or pilihan=="AA":
        idx = 6
    elif pilihan=="bb" or pilihan=="BB":
        idx = 7
    elif pilihan=="cc" or pilihan=="CC":
        idx = 8
    elif pilihan=="dd" or pilihan=="DD":
        idx = 9
    elif pilihan=="ee" or pilihan=="EE":
        idx = 10
    else:
        idx = 0

    #cetak tampilan layar
    print(">>> Pesanan        = " + menu[idx])
    print(">>> Harga          = Rp." + str(harga[idx]))
    print(">>> Jumlah Pesanan = ",qty)

    #hitung transaksi

    fixmenu = menu[idx]
    fixharga = harga[idx]
    fixqty = qty
    total = fixharga * fixqty
    

    #tampilkan total akhir
    print(">>>-------------------------------------")
    print(">>> Total          = Rp." + str(total))
    print(">>>-------------------------------------")
    bayar = int (input(">>> Jumlah Bayar   = Rp."))
    kembalian = bayar-total
    print(">>> Kembalian      = Rp." + str(kembalian))
    print(">>>-------------------------------------")

    pil = input(">> Membuat Transaksi Lain? y/t = ")
    if pil == "t" or pil == "T" :
        break