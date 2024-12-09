class DaftarNilaiMahasiswa:
    def __init__(self):
        self.mahasiswa = []

    def tambah(self, nama, nilai):
        """Menambah data mahasiswa baru."""
        data_mahasiswa = {"nama": nama, "nilai": nilai}
        self.mahasiswa.append(data_mahasiswa)
        print(f"Data mahasiswa {nama} dengan nilai {nilai} berhasil ditambahkan.")

    def tampilkan(self):
        """Menampilkan semua data mahasiswa."""
        if not self.mahasiswa:
            print("Tidak ada data mahasiswa.")
        else:
            print("Daftar Nilai Mahasiswa:")
            for mhs in self.mahasiswa:
                print(f"Nama: {mhs['nama']}, Nilai: {mhs['nilai']}")

    def hapus(self, nama):
        """Menghapus data mahasiswa berdasarkan nama."""
        for mhs in self.mahasiswa:
            if mhs['nama'] == nama:
                self.mahasiswa.remove(mhs)
                print(f"Data mahasiswa {nama} berhasil dihapus.")
                return
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

    def ubah(self, nama):
        """Mengubah data nilai mahasiswa berdasarkan nama."""
        for mhs in self.mahasiswa:
            if mhs['nama'] == nama:
                nilai_baru = input(f"Masukkan nilai baru untuk {nama}: ")
                mhs['nilai'] = nilai_baru
                print(f"Nilai mahasiswa {nama} berhasil diubah menjadi {nilai_baru}.")
                return
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")


# Contoh penggunaan class
daftar_nilai = DaftarNilaiMahasiswa()

# Menambahkan data
daftar_nilai.tambah("sheshe", 90)
daftar_nilai.tambah("adel", 88)

# Menampilkan data
daftar_nilai.tampilkan()

# Mengubah nilai mahasiswa
daftar_nilai.ubah("sheshe")

# Menampilkan data setelah perubahan
daftar_nilai.tampilkan()

# Menghapus data mahasiswa
daftar_nilai.hapus("adel")

# Menampilkan data setelah penghapusan
daftar_nilai.tampilkan()
