#Class Mahasiswa
class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.__nama = nama
        self.__nim = nim
        self.__jurusan = jurusan
        self.__ipk = ipk

    def tampilkan_info(self):
        print(f"Nama    : {self.__nama}")
        print(f"NIM     : {self.__nim}")
        print(f"Jurusan : {self.__jurusan}")
        print(f"IPK     : {self.__ipk}\n")

    def update_ipk(self, nilai_baru):
        if 0.0 <= nilai_baru <= 4.0:
            self.__ipk = nilai_baru
        else:
            print("IPK tidak valid!\n")

    def status_lulus(self):
        if self.__ipk >= 2.5:
            return "Lulus"
        else:
            return "Belum Lulus"

# Program utama
if __name__ == "__main__":
    # Objek mahasiswa
    mhs1 = Mahasiswa("Siti", "220101", "Teknik Informatika", 3.5)
    mhs2 = Mahasiswa("Budi", "220102", "Sistem Informasi")

    # Menampilkan info awal
    mhs1.tampilkan_info()
    mhs2.tampilkan_info()

    # Update IPK
    mhs2.update_ipk(3.8)
    mhs2.tampilkan_info()
    print("Status kelulusan:", mhs2.status_lulus(), "\n")

    # Contoh input IPK tidak valid
    mhs1.update_ipk(4.5)  # IPK tidak valid
    print("Status kelulusan:", mhs1.status_lulus())
