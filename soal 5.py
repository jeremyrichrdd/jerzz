n = int(input("Masukkan nilai N: "))

a, b = 0, 1
i = 1

while i <= n:
    print(b, end=" ")
    x = a
    a = b
    b = x+b
    i += 1