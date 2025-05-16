data_mahasiswa = []

while True:
    print("Menu:")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Keluar")
    pilihan = int(input("Pilih menu (1/2/3/4): "))

    if pilihan == 1:
        nomor = input("Masukkan nomor mahasiswa: ")
        Nama = input("Masukkan nama mahasiswa: ")
        nilai_1 = input("Masukkan nilai mahasiswa: ")

        angka = True
        y = 0
        for v in nilai_1:
            if v == '.':
                y += 1
                if y > 1:
                    angka = False
                    break
            elif v not in '0123456789':
                angka = False
                break

        if angka and nilai_1 != '.':
            nilai = float(nilai_1)
            data_mahasiswa.append([nomor, Nama, nilai])
            print("Data berhasil ditambah!\n")
        else:
            print("Nilai harus berupa angka!\n")

    elif pilihan == 2:
        Nomor_hapus = input("Masukkan nomor mahasiswa yang ingin dihapus: ")
        index_dihapus = -1
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == Nomor_hapus:
                index_dihapus = i
                break

        if index_dihapus != -1:
            del data_mahasiswa[index_dihapus]
            print("Data berhasil dihapus!\n")
        else:
            print("Data tidak ditemukan!\n")

    elif pilihan == 3:
        if len(data_mahasiswa) == 0:
            print("Belum ada data yang tersedia.\n")
        else:
            for i in range(len(data_mahasiswa)):
                for j in range(0, len(data_mahasiswa) - i - 1):
                    if data_mahasiswa[j][2] < data_mahasiswa[j + 1][2]:
                        x = data_mahasiswa[j]
                        data_mahasiswa[j] = data_mahasiswa[j + 1]
                        data_mahasiswa[j + 1] = x

            print("\nData Mahasiswa (Urut Nilai Tertinggi):")
            print("-" * 40)
            print(f"{'No.':<10}{'Nama':<15}{'Nilai':<10}")
            print("-" * 40)
            for mhs in data_mahasiswa:
                print(f"{mhs[0]:<10}{mhs[1]:<15}{mhs[2]:<10.2f}")
            print("-" * 40 + "\n")

    elif pilihan == 4:
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid.\n")
