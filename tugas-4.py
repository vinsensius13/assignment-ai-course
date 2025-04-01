# 1. Mencetak sambutan
print("Selamat datang di program tugas Python!")

# 2. Input nama dan umur
nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))

# 3. Menampilkan pesan tahun depan
print(f"Halo, {nama}! Tahun depan kamu berumur {umur + 1} tahun.")

# 4. List nama mahasiswa
mahasiswa = ["Siti", "Budi", "Andi", "Rina", "Dika"]

print("\nDaftar nama mahasiswa:")
for i, mhs in enumerate(mahasiswa, start=1):
    print(f"{i}. {mhs}")

# 5. Mengecek apakah Budi ada di list
if "Budi" in mahasiswa:
    print("\nBudi ada dalam daftar mahasiswa.")
else:
    print("\nBudi tidak ada dalam daftar mahasiswa.")
    
# Tambahan: cek apakah nama yang diinput pengguna ada di list
if nama.title() in mahasiswa:
    print(f"{nama.title()} ada dalam daftar mahasiswa.")
else:
    print(f"{nama.title()} adalah nama yang tidak terdaftar sebagai mahasiswa.")

# 6. Dictionary data mahasiswa
data_mahasiswa = {
    "220101": "Siti",
    "220102": "Budi",
    "220103": "Andi",
    "220104": "Rina",
    "220105": "Dika"
}

print("\nData Mahasiswa:")
for nim, nama in data_mahasiswa.items():
    print(f"NIM: {nim}, Nama: {nama}")

# 7. Cek angka ganjil/genap
angka = int(input("\nMasukkan sebuah angka: "))
if angka % 2 == 0:
    print(f"Angka {angka} adalah genap.")
else:
    print(f"Angka {angka} adalah ganjil.")
