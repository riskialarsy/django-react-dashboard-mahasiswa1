-- Active: 1723049820932@@127.0.0.1@3306
-- Membuat tabel Mahasiswa
CREATE TABLE Mahasiswa (
    nim VARCHAR(20) PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    jenis_kelamin VARCHAR(20) NOT NULL,
    jurusan VARCHAR(50) NOT NULL,
    fakultas VARCHAR(100) NOT NULL,
    ipk FLOAT NOT NULL,
    semester INTEGER NOT NULL,
    organisasi VARCHAR(100),
    tanggal_lahir DATE NOT NULL,
    asal_kota VARCHAR(50) NOT NULL,
    sks_diambil INTEGER NOT NULL,
    lama_studi INTEGER NOT NULL,
    jalur_masuk VARCHAR(20) NOT NULL,
    tahun_masuk INTEGER NOT NULL
);

-- Memasukkan data contoh ke dalam tabel Mahasiswa
INSERT INTO Mahasiswa (nim, nama, jenis_kelamin, jurusan, fakultas, ipk, semester, organisasi, tanggal_lahir, asal_kota, sks_diambil, lama_studi, jalur_masuk, tahun_masuk)
VALUES 
('12345678', 'Budi Santoso', 'Laki-laki', 'Teknik Informatika', 'Fakultas Teknik', 3.75, 5, 'BEM Fakultas', '2000-05-15', 'Jakarta', 110, 3, 'SNMPTN', 2020),
('23456789', 'Siti Rahayu', 'Perempuan', 'Manajemen', 'Fakultas Ekonomi', 3.60, 3, 'UKM Tari', '2001-08-22', 'Surabaya', 90, 2, 'SBMPTN', 2021),
('34567890', 'Ahmad Fauzi', 'Laki-laki', 'Kedokteran', 'Fakultas Kedokteran', 3.90, 7, 'PMI', '1999-11-30', 'Bandung', 140, 4, 'Mandiri', 2019);


-- Menghapus semua data dari tabel Mahasiswa
DELETE FROM api_mahasiswa;


select * from api_mahasiswa;
