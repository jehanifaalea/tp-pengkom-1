#Koordinat awal robot
x1 = float(input("masukkan koordinat x awal: "))
y1 = float(input("masukkan koordinat y awal: "))

#Koordinat akhir robot
x2 = float(input("masukkan koordinat x akhir: "))
y2 = float(input("masukkan koordinat y akhir: "))

#Kecepatan rata-rata
M = float(input("masukkan nilai kecepatan rata-rata: "))

#perhitungan
x = (x1-x2)
y = (y1-y2)

if x1>= x2:
    x 
else:
    x = x2-x1
   
if y1>= y2:
    y 
else:
    y = y2-y1

s = (x + y)*1.5
if M != 0:
    t = s/M
    print("Robot akan tiba di tujuan setelah", t, "detik")
else:
    print("Kecepatan rata-rata tidak boleh 0")