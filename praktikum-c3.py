nama="Dimas Kurniawan Hendra"
nim="231031088"
meet="Praktikum 3(string)"
prodi="Sistem Informasi C"
email="dimaskrnwn100105@gmail.com"
ttl= "Parepare, 10-Januari-2005"
alamat= "Jalan Kesuma Timur"
asal= "Parepare"
hobi= "Nonton Drakor"
tinggi= "170"
print()
print("-"*110)
str1= "Dimas Kurniawan Hendra"

sp = 110
print("-"*sp)
print(nama.upper().center(sp))
print(nim.center(sp))
print("\n"*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.rjust(sp))
print("-"*sp)
    

print ("""\tHalo, nama saya {nama} dengan NIM {nim} dari prodi{prodi}, ini adalah file {meet}.Terim kasih.\n""")


print(f"""Biodata saya,
nama\t: {nama.upper()}
Nim\t: {nim}
Prodi\t: {prodi}
TTL\t: {ttl}
Alamat\t: {alamat}
Asal\t: {asal}
Hobi\t: {hobi}
Tinggi\t: {tinggi}cm
""")









