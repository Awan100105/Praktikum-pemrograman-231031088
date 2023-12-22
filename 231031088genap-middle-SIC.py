''' UTS
1. Buat variabel jenis list berikut.
    
    Bio =  ['Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'Nama Lengkap',
            'NIM',
            'Tanggal-Bulan-Tahun Lahir',
            'S1',
            'Sistem Informasi C',
            'aktif',
            'ganjil',
            '2023-2024',
            'kartu hasil studi mahasiswa']
#(NOTED: sesuaikan dengan data anda)

2. Buat variabel nested list berikut.

MK =   [['Matkul1','Matkul2','Matkul3','Matkul4','Matkul5','Matkul6','Matkul7','Matkul8'],
        [3,2,3,2,3,3,3,2],
        ['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
        [3.50,3.00,3.75,4.00,3.75,3.50,3.75,3.00]]

#(NOTED: Ubah Nama Matakuliah, Jumlah SKS, dan Nilai)

3. Buat Kode dengan hasil runing seperti berikut.


            INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE
                           JURUSAN SAINS
                    KARTU HASIL STUDI MAHASISWA
                          GANJIL 2023/2024

                    
Nama Lengkap    : NAMA LENGKAP
NIM             : NIM
Program/Prodi   : S1/Sistem Informasi C
Tahun Masuk     : 2023-Ganjil
Status          : Aktif
|--|--   12   --|--             31            --|-- 7 --|--    13   --|
-----------------------------------------------------------------------
No. Kode        |           Mata Kuliah         |  SKS  | Nilai (0-4) |
-----------------------------------------------------------------------
1   22A1209     | Matkul1                       |   3   |         3.50|
2   22A1210     | Matkul2                       |   2   |         3.00|
3   22A1211     | Matkul3                       |   3   |         3.75|
4   22A1212     | Matkul4                       |   2   |         4.00|
5   22A1213     | Matkul5                       |   3   |         3.75|
6   22A1214     | Matkul6                       |   3   |         3.50|
7   22A1215     | Matkul7                       |   3   |         3.75|
8   22A1216     | Matkul8                       |   2   |         3.00|
-----------------------------------------------------------------------
                                       TOTAL SKS:   21
-----------------------------------------------------------------------
|---------------------------------71-----------------------------------|
Summary:
Jumlah Mata Kuliah : 8 Mata Kuliah
Nilai Tertinggi    : 4.00  (22A1212 - Matkul4)
Nilai Terendah     : 3.00  (22A1211 - Matkul2)
IP Kumulatif       : 3.00
                                   
                                               Parepare, 25 Oktober 2023



                                                     NAMA LENGKAP      
                                                     ------------
'''


# Tulis Kode Jawaban di bawah!

#1. Buat variabel jenis list berikut.
    
Bio =  ['Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'Dimas Kurniawan Hendra',
            '231031088',
            '10-Januari-2005',
            'S1',
            'Sistem Informasi C',
            'aktif',
            'ganjil',
            '2023-2024',
            'kartu hasil studi mahasiswa']

#2. Buat variabel nested list berikut.

MK =   [['Agama Islam','Pancasila','Bahasa Indonesia','Cinta','Pengantar Pemrograman','PTI','Kalkulus Dasar 1','Sains Terpadu'],
        [3,2,3,2,3,3,3,2],
        ['22B1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
        [3.50,3.00,3.75,4.00,3.75,3.50,3.75,3.00]]

#3. Buat Kode dengan hasil runing seperti berikut.

print(Bio[0].upper().center(71))
print(Bio[2].upper().center(71))
print(Bio[-1].upper().center(71))
strr = Bio[-3]+' '+Bio[-2].replace('-','/')
print(strr.upper().center(71))


print(f'''
Nama lengkap    : {Bio[3].upper()}
NIM             : {Bio[4]}
Programan/prodi : {Bio[-5]}/{Bio[2]}
Tahun masuk     : {Bio[-2][:4]} {Bio[-3].title()}
Status          : {Bio[-4]}''')

print()

print('-'*71)
print("|--|--   12   --|--             26            --|-- 7 --|--    13   --|")
print('No.'+'|'+'kode'.ljust(10)+'|'+'Mata Kuliah'.center(26)+'|'+'SKS'.center(5)+'|'+'Nilai (0-4)'.center(8)+'|')
print('-'*71)
print('1.'+'|'+'22A1209'.ljust(10)+'|'+'Agama Islam'.center(26)+'|'+'3'.center(5)+'|'+'3.50'.center(8)+'|')
print('2.'+'|'+'22A1210'.ljust(10)+'|'+'Pancasila'.center(26)+'|'+'2'.center(5)+'|'+'3.00'.center(8)+'|')
print('3.'+'|'+'22A1211'.ljust(10)+'|'+'Bahasa Indonesia'.center(26)+'|'+'3'.center(5)+'|'+'3.75'.center(8)+'|')
print('4.'+'|'+'22A1212'.ljust(10)+'|'+'Cinta'.center(26)+'|'+'2'.center(5)+'|'+'4.00'.center(8)+'|')
print('5.'+'|'+'22A1213'.ljust(10)+'|'+'Pengantar Pemrograman'.center(26)+'|'+'3'.center(5)+'|'+' 3.75'.center(8)+'|')
print('6.'+'|'+'22A1214'.ljust(10)+'|'+'PTI'.center(26)+'|'+'3'.center(5)+'|'+'3.50'.center(8)+'|')
print('7.'+'|'+'22A1215'.ljust(10)+'|'+'Kalkulus Dasar 1'.center(26)+'|'+'3'.center(5)+'|'+' 3.75'.center(8)+'|')
print('8.'+'|'+'22A1216'.ljust(10)+'|'+'Sains Terpadu'.center(26)+'|'+'2'.center(5)+'|'+'3.00'.center(8)+'|')
print('-'*71)

print("-----------------------------------------------------------------------")
print(f"                                       TOTAL SKS:   {sum(MK[1])}")
print("-----------------------------------------------------------------------")
print("|---------------------------------71-----------------------------------|")
print(f"Summary:")
print(f"Jumlah Mata Kuliah : {len(MK[0])} Mata Kuliah")
print(f"Nilai Tertinggi    : {max(MK[3]):.2f}  ({MK[2][MK[3].index(max(MK[3]))]} - {MK[0][MK[3].index(max(MK[3]))]})")
print(f"Nilai Terendah     : {min(MK[3]):.2f}  ({MK[2][MK[3].index(min(MK[3]))]} - {MK[0][MK[3].index(min(MK[3]))]})")
print(f"IP Kumulatif       : {sum(MK[3])/len(MK[3]):.2f}\n")

print(f"{Bio[1]}, 25 Oktober 2023\n\n")

print(f"{Bio[3]:<54}")
print("                                                     ------------")

print()

