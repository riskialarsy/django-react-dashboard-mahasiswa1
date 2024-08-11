import random
from datetime import datetime, timedelta
import sqlite3

# Daftar jurusan dan fakultas
jurusan_fakultas = {
    "Teknik Informatika": "Fakultas Teknik",
    "Manajemen": "Fakultas Ekonomi dan Bisnis",
    "Psikologi": "Fakultas Psikologi",
    "Hukum": "Fakultas Hukum",
    "Kedokteran": "Fakultas Kedokteran"
}

# Fungsi untuk menghasilkan tanggal lahir acak
def tanggal_lahir_acak():
    start_date = datetime(1995, 1, 1)
    end_date = datetime(2003, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + timedelta(days=random_number_of_days)

# Membuat koneksi ke database SQLite
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Membuat tabel mahasiswa jika belum ada
cursor.execute('''CREATE TABLE IF NOT EXISTS mahasiswa
                  (nim TEXT PRIMARY KEY,
                   nama TEXT,
                   jenis_kelamin TEXT,
                   jurusan TEXT,
                   fakultas TEXT,
                   ipk REAL,
                   semester INTEGER,
                   organisasi TEXT,
                   tanggal_lahir TEXT,
                   asal_kota TEXT,
                   sks_diambil INTEGER,
                   lama_studi INTEGER,
                   jalur_masuk TEXT,
                   tahun_masuk INTEGER)''')

# Membuat data mahasiswa dan memasukkan ke database
for i in range(1, 20):  # Membuat 199 data mahasiswa
    nim = f"2024{i:04d}"
    nama = f"Mahasiswa {i}"
    jenis_kelamin = random.choice(["Laki-laki", "Perempuan"])
    jurusan = random.choice(list(jurusan_fakultas.keys()))
    fakultas = jurusan_fakultas[jurusan]
    ipk = round(random.uniform(2.0, 4.0), 2)
    semester = random.randint(1, 8)
    organisasi = random.choice(["BEM", "Himpunan", "UKM", "Tidak Ada"])
    tanggal_lahir = tanggal_lahir_acak().strftime("%Y-%m-%d")
    asal_kota = random.choice(["Jakarta", "Surabaya", "Bandung", "Yogyakarta", "Semarang", "Medan", "Makassar"])
    sks_diambil = random.randint(18, 24)
    lama_studi = random.randint(6, 14)
    jalur_masuk = random.choice(["SNMPTN", "SBMPTN", "Mandiri"])
    tahun_masuk = 2024 - (semester // 2)

    # Memasukkan data ke database
    cursor.execute('''
    INSERT INTO api_mahasiswa (nim, nama, jenis_kelamin, jurusan, fakultas, ipk, semester, organisasi, tanggal_lahir, asal_kota, sks_diambil, lama_studi, jalur_masuk, tahun_masuk)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (nim, nama, jenis_kelamin, jurusan, fakultas, ipk, semester, organisasi, tanggal_lahir, asal_kota, sks_diambil, lama_studi, jalur_masuk, tahun_masuk))

# Commit perubahan dan menutup koneksi
conn.commit()
conn.close()

print("Data mahasiswa berhasil dimasukkan ke database SQLite.")
