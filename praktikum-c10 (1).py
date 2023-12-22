import os

a = True
while a:
    os.system('clear')

    # judul 
    print('PROGRAM MENGHITUNG VOLUME DAN LUAS PERMUKAAN')
    print('BANGUN RUANG BALOK')
    print()

    # inputan
    p = float(input('Masukkan Panjang: '))
    l = float(input('Masukkan Lebar: '))
    t = float(input('Masukkan Tinggi: '))

    # perhitungan
    vol = p * l * t
    luas = 2 * (p*l + p*t + l*t)
    luas_non_tutup = luas - p*l

    # tampilkan
    print(f'Nilai dari volume adalah : {vol}')
    print(f'Nilai dari luas permukaan adalah : {luas}')
    print(f'Nilai dari luas permukaan tanpa tutup adalah : {luas_non_tutup}')

    # pilihan
    pilih = input('Apakah lanjutkan? [y/n]')
    if pilih == 'y':
        a = True
    else:
        a = False
        print('Sampai jumpa lagi,')