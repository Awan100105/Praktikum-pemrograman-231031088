#latihan 3
# Terima input nama karyawan dari pengguna
nama = input("Masukkan nama karyawan: ")

# Terima input pendapatan karyawan dari pengguna dan mengonversinya ke integer
pendapatan = int(input("Masukkan besaran pendapatan karyawan: "))

# Cetak nama karyawan
print("Nama karyawan:", nama)

# Cetak pendapatan karyawan
print("Pendapatan karyawan:", pendapatan)

# Periksa apakah pendapatan lebih besar dari 1000
if pendapatan > 1000:
    print("Status: Berhak")
else:
    print("Status: Tidak Berhak")