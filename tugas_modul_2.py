#Daftar Menu
print('''
                DAFTAR MENU 
       ___________________________________
      |PAKET|       ISI       |   HARGA   |
      |_____|_________________|___________|
      |  A  |- Nasi Putih     |           |
      |     |- Ayam Goreng    |           |
      |     |- Tahu + Tempe   |           |
      |     |- Lalap Sambal   | Rp20.000  |
      |     |- Kerupuk        |           |
      |     |- Es Teh         |           |
      |_____|_________________|___________|
      |  B  |- Nasi Kuning    |           |
      |     |- Ayam Goreng    |           |
      |     |- Tahu + Tempe   |           |
      |     |- Kerupuk        | Rp25.000  |
      |     |- Sambal Bawang  |           |
      |     |- Es Teh         |           |
      |_____|_________________|___________|
      |  C  |- Nasi Kuning    |           |
      |     |- Telur Balado   |           |
      |     |- Ayam goreng    |           |
      |     |- Sambal Tomat   | Rp35.000  |
      |     |- Acar           |           |
      |     |- Kerupuk        |           |
      |     |- Es Teh         |           |
      |_____|_________________|___________|
      |  D  |- Nasi Goreng    |           |
      |     |- telur Dadar    |           |
      |     |- Sate Ayam      |           |
      |     |- Acar           | Rp40.000  |
      |     |- Sambal Bawang  |           |
      |     |- Es Teh         |           |
      |_____|_________________|___________|
      |  E  |- Nasi Uduk      |           |
      |     |- Ayam Bakar     |           |
      |     |- Sambal Kentang |           |
      |     |- Telur Balado   | Rp45.0000 |
      |     |- Saayur Lodeh   |           |
      |     |- Kerupuk Kulit  |           |
      |     |- Es Teh         |           |
      |_____|_________________|___________|
      ''')

# input data
Nama    = input("Masukkan nama: ")
Alamat  = input("masukkan alamat: ")
No_telp = input("Maukkan No.Telpon: ")

# Pemilihan paket
pesanan = {}
while True:
    paket = input("Pilih paket (A/B/C/D/E) atau ketik 'selesai' untuk selesai: ").upper()
    if paket == "SELESAI":
        break
    elif paket in ["A", "B", "C", "D", "E"]:
        jumlah = int(input("Masukkan jumlah paket: "))
        if paket == "A": harga_per_paket = 20000
        elif paket == "B": harga_per_paket = 25000
        elif paket == "C": harga_per_paket = 35000
        elif paket == "D": harga_per_paket = 40000
        elif paket == "E": harga_per_paket = 45000
        
        pesanan[paket] = pesanan.get(paket, 0) + jumlah
        harga = harga_per_paket * jumlah
    else:
        print("Paket tidak valid, silakan pilih lagi.")
        

#total harga
pajak = harga*0.1
biaya_pengiriman = 0 if harga>=150000 else 25000
total_harga = harga + pajak + biaya_pengiriman

#Struk

print("\n *STRUK PEMBELIAN* ")
print ("\nNama : ",Nama)
print("No.Telepon : ",No_telp)
print("Alamat Pengiriman : ", Alamat)

print("\nDetail Pesanan:")
for kode, jumlah in pesanan.items():
    print(f"Paket {kode} x{jumlah}")

print("\nRincian Harga: ")
print("Harga = Rp", harga)
print("Pajak (10%) = Rp", pajak)
print("Biaya Pengiriman = Rp", biaya_pengiriman)
print("Total Harga = Rp", total_harga)

print("\n= TERIMAKASI TELAH MEMBELI =")