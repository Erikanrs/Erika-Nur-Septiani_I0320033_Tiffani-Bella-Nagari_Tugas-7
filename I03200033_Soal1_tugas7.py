print("="*60)
judul = "Program Memperkenalkan Diri"
center = judul.center(50,"*")
print(center)
print("="*50)

sapaan = input("Masukkan kalimat sapaan anda: ")
print(sapaan)
print("Jumlah huruf kalimat sapaan anda: ", len(sapaan), "huruf")

Nama = input("Siapa nama anda: ")
kapital = Nama.capitalize()
print("Nama saya adalah: ", kapital)

kenaldiri = (sapaan,"nama saya", kapital)

kenaldiri1 = kenaldiri.upper()
kenaldiri2 = kenaldiri.lower()
print("Kalimat sapaan anda dalam huruf kapital: ", kenaldiri1)
print("Kalimat sapaan anda dalam huruf kecil: ", kenaldiri2)

a = kenaldiri.count("a")
i = kenaldiri.count("i")
u = kenaldiri.count("u")
e = kenaldiri.count("e")
o = kenaldiri.count("o")
print("Jumlah huruf a dalam kalimat perkenalan anda = ", a, "huruf")
print("Jumlah huruf i dalam kalimat perkenalan anda = ", i, "huruf")
print("Jumlah huruf u dalam kalimat perkenalan anda = ", u, "huruf")
print("Jumlah huruf e dalam kalimat perkenalan anda = ", e, "huruf")
print("Jumlah huruf o dalam kalimat perkenalan anda = ", o, "huruf")