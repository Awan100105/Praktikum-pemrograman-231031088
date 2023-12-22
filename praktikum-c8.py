import os
import random as rd
os.system('clear')

warna = ['merah','putih','hitam']
com = rd.choice(warna)
a = True
limit = 3
i = 0

while a:
    pilih = input('Masukkan Pilihan [merah,putih,hitam]: ')
    if pilih == com:
        print(f'Pilihan anda benar yaitu {pilih} \n')
        a = False
    else:
        if i < limit:
           print('Tebakan anda salah!')
           print(f'Kesempatan Anda tersisa {limit-i} kali')
           a = True 
        else:
            print('Kesempatan anda habis!')
            a = False