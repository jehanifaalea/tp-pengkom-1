level1 = int(input("Banyak pemain yang memainkan level 1: "))
selesai1 = int(input("Banyak pemain berhasil menyelesaikan level 1: "))
level2 = int(input("Banyak pemain yang memainkan level 2: "))
selesai2 = int(input("Banyak pemain berhasil menyelesaikan level 2: "))
level3 = int(input("Banyak pemain yang memainkan level 3: "))
selesai3 = int(input("Banyak pemain berhasil menyelesaikan level 3: "))
level4 = int(input("Banyak pemain yang memainkan level 4: "))
selesai4 = int(input("Banyak pemain berhasil menyelesaikan level 4: "))
level5 = int(input("Banyak pemain yang memainkan level 5: "))
selesai5 = int(input("Banyak pemain berhasil menyelesaikan level 5: "))


#perhitungan
lvl1 = selesai1/level1
lvl2 = selesai2/level2
lvl3 = selesai3/level3
lvl4 = selesai4/level4
lvl5 = selesai5/level5

Mudah = 0
Sedang = 0
Sulit = 0
#level 1
if lvl1 >= 0.8:
    Mudah += 1
elif 0.3 <= lvl1 < 0.8:
    Sedang += 1
else:
    Sulit += 1

#level 2
if lvl2 >= 0.8:
    Mudah += 1
elif 0.3 <= lvl2 < 0.8:
    Sedang += 1
else:
    Sulit += 1

#Level 3
if lvl3 >= 0.8:
    Mudah += 1
elif 0.3 <= lvl3 < 0.8:
    Sedang += 1
else:
    Sulit += 1

#Level 4
if lvl4 >= 0.8:
    Mudah += 1
elif 0.3 <= lvl4 < 0.8:
    Sedang += 1
else:
    Sulit += 1

#Level 5
if lvl5 >= 0.8:
    Mudah += 1
elif 0.3 <= lvl5 < 0.8:
    Sedang += 1
else:
    Sulit += 1

print("Banyak level mudah sebanyak", Mudah,"," "level sedang sebanyak", Sedang,"," "dan level sulit sebanyak" ,Sulit, ".")

#Target
target = Mudah >= 2 and Sulit >= 1
if target :
    print("Target berhasil tercapai")
else:
    print("Target gagal dicapai")