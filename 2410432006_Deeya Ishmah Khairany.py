lambda_t = float(input("Masukkan nilai λt: "))
M = int(input("Masukkan nilai M: "))

# Nilai e secara manual
e = 2.71828

for n in range(M + 1):
    faktorial = 1
    for i in range(1, n + 1):
        faktorial *= i
    print(f"P(N(t) = {n}) =", (e**(-lambda_t) * lambda_t**n) / faktorial)
