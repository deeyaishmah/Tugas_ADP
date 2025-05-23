print("=== Program Penghitung Jarak Antar Titik ===")

# Meminta jumlah titik
valid = False
while not valid:
    n_input = input("Masukkan jumlah titik (n): ")
    if n_input.isdigit():
        n = int(n_input)
        if n >= 2:
            valid = True
        else:
            print("Minimal 2 titik.")
    else:
        print("Masukkan angka bulat yang valid.")

# Input titik 
titik = []
for i in range(n):
    valid = False
    while not valid:
        koordinat = input(f"Masukkan koordinat titik ke-{i+1} (format: x y): ").strip().split()
        if len(koordinat) == 2:
            x_str, y_str = koordinat[0], koordinat[1]
            if (x_str[0] == '-' and x_str[1:].isdigit()) or x_str.isdigit():
                if (y_str[0] == '-' and y_str[1:].isdigit()) or y_str.isdigit():
                    x = int(x_str)
                    y = int(y_str)
                    titik.append([x, y])
                    valid = True
                else:
                    print("Koordinat y harus angka bulat.")
            else:
                print("Koordinat x harus angka bulat.")
        else:
            print("Input harus 2 angka bulat, pisahkan dengan spasi.")

# Menampilkan titik-titik
print("\nKumpulan titik:")
for i in range(n):
    print(f"Titik {i+1}: ({titik[i][0]}, {titik[i][1]})")

# Hitung jarak antar titik
print("\n=== Jarak Antar Titik ===")
for i in range(n):
    for j in range(i + 1, n):
        dx = titik[i][0] - titik[j][0]
        dy = titik[i][1] - titik[j][1]
        jarak = (dx*dx + dy*dy) ** 0.5
        print(f"Jarak Titik {i+1} ke Titik {j+1}: {jarak:.2f}")
