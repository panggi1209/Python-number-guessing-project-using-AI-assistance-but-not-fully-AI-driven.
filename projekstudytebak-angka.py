# Projek Latihan 
#by panggi yulian p
import random

print("=== Game Tebak Angka  1-25 ===") #menampilkan judul game 
angka_rahasia = random.randint (1,25)  #Menghasilkan angka random  antara 1-25
tebakan = 0  #Inisialisasi variabel tebakan dengan nilai 0

while tebakan != angka_rahasia :  #Selama tebakan tidak sama dengan angka_rahasia, ulangi proses berikut
    tebakan = int(input("Tebak Angka (1-25):"))  # Input dari user untuk menebak angka -->
    if tebakan < angka_rahasia:   # komponen if elif dan else dalam python harus diakhiri dengan titik dua (:) dan harus sejajar dengan tebakan
         print("Terlalu kecil!")
    elif tebakan > angka_rahasia:
            print("Terlalu besar!")
    else :
            print("🎉 Selamat, tebakanmu benar!" )

import random
