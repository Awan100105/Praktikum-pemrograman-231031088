def hitung_faktorial(nilai):
    # Mencari Faktorial dengan input
    if nilai > 1:
        return nilai * hitung_faktorial(nilai - 1)
    return 1

# Meminta input dari pengguna
nilai = int(input("Masukkan nilai yang akan dihitung faktorialnya: "))

# Program Utama mulai di sini
faktorial = hitung_faktorial(nilai)
print(f'Nilai Faktorial dari {nilai}! = {faktorial}')