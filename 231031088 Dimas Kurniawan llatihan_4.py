#latihan 4
# Terima input pendapatan dari pengguna dan mengonversinya ke integer
pendapatan = int(input("Masukkan besaran pendapatan karyawan: "))

# Pernyataan if...elif...else untuk mengecek persentase bonus
if pendapatan <= 1000:
    persentase = 0
elif pendapatan <= 2000:
    persentase = 10
elif pendapatan <= 3000:
    persentase = 20
elif pendapatan <= 4000:
    persentase = 30
elif pendapatan <= 5000:
    persentase = 40

# Menghitung bonus
bonus = pendapatan * (persentase / 100)

# Menghitung pendapatan
total = pendapatan + bonus

# Cetak output
print("Pendapatan :", pendapatan)
print("Persentase :", persentase, "%")
print("Bonus :", bonus)
print("Total pendapatan:", total)