# Ukuran kursi
m, n = 20, 5  # Total kursi 20x5 = 100
kursi = list(range(1, m * n + 1))

def tampilkan_kursi():
    print("\nLayout Kursi:")
    for i in range(20):
        row = kursi[i * 5:(i + 1) * 5]
        print(" ".join(f"{k:2}" if k != 0 else "--" for k in row))
        

# Harga tiket berdasarkan kategori
harga_kategori = {
    "VVIP": 1200000,
    "VIP": 1000000,
    "Reguler": 800000,
    "Ekonomi": 500000
}        

def kategori_kursi(nomor_kursi):
    if nomor_kursi <= 10:
        return "VVIP"
    elif nomor_kursi <= 25:
        return "VIP"
    elif nomor_kursi <= 75:
        return "Reguler"
    else:
        return "Ekonomi"

def pesan_tiket():
    jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dipesan: "))
    for _ in range(jumlah_tiket):
        nama = input("Masukkan nama Anda: ")
        while True:
            nomor_kursi = int(input("Masukkan nomor kursi yang ingin dipesan: "))
            if nomor_kursi in kursi:
                kursi[kursi.index(nomor_kursi)] = 0  
                kategori = kategori_kursi(nomor_kursi)
                harga = harga_kategori[kategori]
                password = input("Buat password : ")
                pemesanan.append((nama, nomor_kursi, kategori, harga, password))
                break
            else:
                print("Kursi tidak tersedia! Pilih kursi lain.")

def tampilkan_struk():
    for nama, nomor_kursi, kategori, harga, password in pemesanan:
        print(f"\n=== Struk Pemesanan ===\nNama: {nama}\nNomor Kursi: {nomor_kursi}\nKategori: {kategori}\nHarga: Rp{harga:,}\nPassword: {password}\n")



pemesanan = []

tampilkan_kursi()
pesan_tiket()
tampilkan_struk()
tampilkan_kursi()
print("\nTerima kasih telah melakukan reservasi!")

