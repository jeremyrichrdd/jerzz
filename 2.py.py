jumlah_data = int(input("Masukkan berapa banyak angka: "))

total = 0
i = 1

while i <= jumlah_data:
    angka = float(input(f"Masukkan angka ke {i}: "))
    total = total + angka
    i = i+1     

rata_rata = total / jumlah_data

print(f"Rata-rata dari {jumlah_data} angka tersebut adalah: {rata_rata}")