n = int(input("Masukkan nilai N: "))

faktor = 1
i = 1

while i <= n:
    faktor = faktor * i
    i = i+1

print(f"Faktorial dari {n} adalah {faktor}")