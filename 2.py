#Daftar Menu
print('''
                              =PAKET HEMAT= 
 _________________________________    __________________________________
|PAKET|       ISI     |   HARGA   |  |PAKET|       ISI      |   HARGA   | 
|_____|_______________|___________|  |_____|________________|___________|
|  A  |- Nasi Putih   |           |  |  D  |- Nasi Goreng   |           |
|     |- Ayam Goreng  |           |  |     |- telur Dadar   |           |
|     |- Tahu + Tempe | Rp20.000  |  |     |- Sate Ayam     | Rp40.000  |
|     |- Es Teh       |           |  |     |- Sambal Bawang |           |
|_____|_______________|___________|  |     |- Es Teh        |           |
|  B  |- Nasi Kuning  |           |  |_____|________________|___________|
|     |- Ayam Goreng  |           |  |  E  |- Nasi Uduk     |           |
|     |- Tahu + Tempe | Rp25.000  |  |     |- Ayam Bakar    |           |
|     |- Sambal Bawang|           |  |     |- Sambal Kentang|           |
|     |- Es Teh       |           |  |     |- Telur Balado  | Rp45.0000 |
|_____|_______________|___________|  |     |- Sayur Lodeh   |           |
|  C  |- Nasi Kuning  |           |  |     |- Es Teh        |           |
|     |- Telur Balado |           |  |_____|________________|___________|
|     |- Ayam goreng  |           |
|     |- Sambal Tomat | Rp35.000  |
|     |- Es Teh       |           |
|_____|_______________|___________|
    ''')

# input data
Nama    = input("Masukkan nama: ")
Alamat  = input("masukkan alamat: ")
No_telp = input("Maukkan No.Telpon: ")

# Pemilihan paket
paket = input ("Pilih Paket Hemat (A/B/C/D/E): ").upper()
jumlah = int(input("Masukkan Jumlah Paket: "))

if paket == "A":
    harga_per_paket = 20000
elif paket == "B":
     harga_per_paket = 25000
elif paket == "C":
     harga_per_paket = 35000
elif paket == "D":
     harga_per_paket = 40000
elif paket == "E":
     harga_per_paket = 45000
else:
    print("paket tidak valid, silahkan ulangi")
    
harga= harga_per_paket*jumlah

#total harga
pajak = harga*0.1
biaya_pengiriman = 0 if harga>=150000 else 25000
total_harga = harga + pajak + biaya_pengiriman

#Struk

print("\n =STRUK PEMBELIAN= ")
print ("\nNama : ",Nama)
print("No.Telepon : ",No_telp)
print("Alamat Pengiriman : ", Alamat)

print("\nDetail Pesanan: " )
print("Paket ", paket ,"x", jumlah, "Paket")

print("\nRincian Harga: ")
print("Harga = Rp", harga)
print("Pajak (10%) = Rp", pajak)
print("Biaya Pengiriman = Rp", biaya_pengiriman)
print("Total Harga = Rp", total_harga)

print("\n= TERIMAKASI TELAH MEMBELI =")
