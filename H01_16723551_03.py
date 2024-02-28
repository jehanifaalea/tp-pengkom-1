# NIM/Nama : 16723551/ Jehanifa Taufiq Alea
# Tanggal : 28 Februari 2024
# Deskripsi : Pengerjaan soal TP pertama tentang input dan percabangan

tas_a = float(input("Masukkan berat tas A: "))
tas_b = float(input("Masukkan berat tas B: "))
tas_c = float(input("Masukkan berat tas C: "))
batas_seluruhnya = float(input("Masukkan batasan berat tas keseluruhan: "))
batas_kabin = float(input("Masukkan batasan berat tas yang dibawa ke kabin: "))

total_berat = tas_a + tas_b + tas_c
peraturan_1 = total_berat <= batas_seluruhnya
langgar_1 = total_berat > batas_seluruhnya
peraturan_2 = tas_a <= batas_kabin or tas_b <= batas_kabin or tas_c <= batas_kabin
langgar_2 = tas_a > batas_kabin or tas_b > batas_kabin or tas_c > batas_kabin

if peraturan_1 and peraturan_2:
    print("Tuan Kil memenuhi kebijakan maskapai.")
elif peraturan_1 and langgar_2:
    print("Tuan Kil melanggar peraturan 2 kebijakan maskapai")
elif peraturan_2 and langgar_1:
    print("Tuan Kil melanggar peraturan 1 kebijakan maskapai")
else:
    print("Tuan Kil melanggar peraturan 1 dan 2 kebijakan maskapai")

