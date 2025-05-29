def input_data():
    data = []
    n = int(input("Masukkan jumlah praktikan: "))
    i = 0
    while i < n:
        print("Data Praktikan ke-", i + 1)
        nama = input("Nama: ")
        nim = input("NIM: ")
        pretest = float(input("Nilai pretest: "))
        postest = float(input("Nilai postest: "))
        tugas = float(input("Nilai tugas/makalah: "))
        bonus = float(input("Nilai bonus: "))
        praktikan = [nama, nim, pretest, postest, tugas, bonus, 0, 0]
        data.append(praktikan)
        i = i + 1
    return data

def hitung_rata_preposttugas(data):
    total_pre = 0
    total_post = 0
    total_tugas = 0
    i = 0
    while i < len(data):
        total_pre = total_pre + data[i][2]
        total_post = total_post + data[i][3]
        total_tugas = total_tugas + data[i][4]
        i = i + 1
    rata_pre = total_pre / len(data)
    rata_post = total_post / len(data)
    rata_tugas = total_tugas / len(data)
    return rata_pre, rata_post, rata_tugas

def hitung_nilai_akhir(data):
    i = 0
    while i < len(data):
        pre = data[i][2]
        post = data[i][3]
        tugas = data[i][4]
        bonus = data[i][5]
        nilai_akhir = (0.25 * pre) + (0.25 * post) + (0.5 * tugas) + bonus
        data[i][6] = nilai_akhir
        i = i + 1

def urutkan_dan_peringkat(data):
    i = 0
    while i < len(data) - 1:
        j = 0
        while j < len(data) - i - 1:
            if data[j][6] < data[j + 1][6]:
                x = data[j]
                data[j] = data[j + 1]
                data[j + 1] = x
            j = j + 1
        i = i + 1
    i = 0
    while i < len(data):
        data[i][7] = i + 1
        i = i + 1

def hitung_rata_nilai_akhir(data):
    total = 0
    i = 0
    while i < len(data):
        total = total + data[i][6]
        i = i + 1
    return total / len(data)

def tampilkan_tabel(data, rata_akhir):
    print("\n===============================================================")
    print("Nama\t\tNIM\t\tNilai Akhir\tPeringkat")
    print("---------------------------------------------------------------")
    i = 0
    while i < len(data):
        nama = data[i][0]
        nim = data[i][1]
        nilai = data[i][6]
        peringkat = data[i][7]

    
        if len(nama) < 8:
            spasi_nama = "\t\t"
        else:
            spasi_nama = "\t"

        print(nama + spasi_nama + nim + "\t" + str(nilai) + "\t" + str(peringkat))
        i = i + 1

    print("===============================================================")
    print("Rata-rata nilai akhir: " + str(rata_akhir))

# Program utama
praktikan_data = input_data()
rata_pre, rata_post, rata_tugas = hitung_rata_preposttugas(praktikan_data)
hitung_nilai_akhir(praktikan_data)
urutkan_dan_peringkat(praktikan_data)
rata_akhir = hitung_rata_nilai_akhir(praktikan_data)
tampilkan_tabel(praktikan_data, rata_akhir)
