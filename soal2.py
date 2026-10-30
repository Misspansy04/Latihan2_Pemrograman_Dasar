pilihan = int(input("Pilih 1 (keliling) atau 2 (luas): "))
r = float (input("Masukkan jari-jari: "))
if pilihan == 1:
    print ("Keliling =", 2 * 3.14 * r)
elif pilihan == 2:
    print ("Luas =", 3.14 * r ** 2)
else:
    print("Pilihan tidak valid")