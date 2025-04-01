# Fungsi untuk menghitung rata-rata
def hitung_rata_rata(nilai_list):
    if len(nilai_list) == 0:
        return 0
    return round(sum(nilai_list) / len(nilai_list), 2)

# Kelas Mahasiswa
class Mahasiswa:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

    def tampilkan_info(self):
        rata_rata = hitung_rata_rata(self.nilai)
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Rata-rata nilai: {rata_rata}\n")

    def tambah_nilai(self, nilai_baru):
        self.nilai.append(nilai_baru)

# Program utama
if __name__ == "__main__":
    mhs1 = Mahasiswa("Budi", "220101", [80, 85, 90])
    mhs2 = Mahasiswa("Siti", "220102", [75, 80, 70])

    mhs1.tampilkan_info()
    mhs2.tampilkan_info()

    print("Menambahkan nilai baru...")
    mhs1.tambah_nilai(95)
    mhs1.tampilkan_info()