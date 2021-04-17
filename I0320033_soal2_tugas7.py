print("="*60)
print("Program Menghitung Berat Badan Siswa")
print("="*60)

berat_siswa = input("Masukkan berat badan siswa (pisahkan dengan spasi): ").split()

for i in range(len(berat_siswa)):
    berat_siswa[i] = int(berat_siswa[i])

print("Berat badan yang diinput : ", berat_siswa)


rata_rata = sum(berat_siswa)/len(berat_siswa)
print("Rata-rata berat badan siswa adalah ", rata_rata)

import math
print("Berat badan yang paling tinggi adalah ", max(berat_siswa))

print("Berat badan yang paling rendah adalah ", min(berat_siswa))

print("Rata-rata berat badan dengan pembulatan ke atas adalah ", math.ceil(rata_rata))

print("Rata-rata tberat badan dengan pembulatan ke bawah adalah ", math.floor(rata_rata))