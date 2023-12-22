import os
os.system("clear")

nim = ("3","2","1","0","3","1","0","8","8")

print(nim)

print("item indeks 0 (pertama)",nim[0])
print("item indeks 1 (kedua)",nim[1])

print(f"item indeks 0 (pertama) {nim[0]}")
print(f"item indeks 1 (kedua) {nim[1]}")
print(f"item indeks 1 terakhir {nim[len(nim)-1]}")
print(f"item indeks 1 terakhir {nim[-1]}")
print(f"item indeks 1 (pertama) {nim[-len(nim)]}")

data = ["Dimas Kurniawan Hendra",2023,"Aktif"]
nilai= [90,89,93,97]

print("Nama: "+ data[0])
print("angkatan:", data[1])
print("status: "+ data[2])
#Dimas Kurniawan Hendra status Kuliah: Aktif
print(f"{data[0]} status kuliah : {data[2]}")

#Data terbesar nilai adalah: 97
print(f"Data terbesar adalah : {max(nilai)}")

#Data terkecil nilai adalah: 89
print(f"Data terkecil adalah : {min(nilai)}")

#Rata-rata nilai adalah: 92.25
a= sum(nilai) / (len(nilai))
print(f"Rata-rata nilai adalah : {a}")

data = ("mahasiswa1",2023,"Aktif")
nilai= (90,89,93,97)

print(data[1])
print(data[-1])
print(nilai[1:-1])

#Jumlah nilai mahasiswa adalah: 4
print(f"Jumlah nilai {data[0]} adalah: {len(nilai)}")

data = [("Dimas Kurniawan Hendra",2023,"Aktif"),

(90,89,93,97),
(20,22),
("S1-Reguler","Ganjil")]

print(data[0][0])
print(data[-1][0])
print(data[2][0:])

#Nama mahasiswa: Dimas Kurniawan Hendra
print(f"Nama mahasiswa: {data[0][0]}")

#Inisial Dimas Kurniawan Hendra: D K H
print(f"Inisial Dimas Kurniawan Hendra: {data[0][0][0]} {data[0][0][6]} {data[0][0][15]}")

#NIM Dimas Kurniawan Hendra: 231031088
print(f"NIM Dimas Kurniawan Hendra: {nim[0]}{nim[1]}{nim[2]}{nim[3]}{nim[4]}{nim[5]}{nim[6]}{nim[7]}{nim[8]} ")

#Program Dimas Kurniawan Hendra: S1-Reguler Sistem Informasi C
print(f"Program Dimas Kurniawan Hendra: {data[-1]}")







