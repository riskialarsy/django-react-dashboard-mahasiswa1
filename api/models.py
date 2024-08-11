from django.db import models

class Mahasiswa(models.Model):
    nim = models.CharField(max_length=20, primary_key=True)
    nama = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=20)
    jurusan = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    ipk = models.FloatField()
    semester = models.IntegerField()
    organisasi = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    asal_kota = models.CharField(max_length=50)
    sks_diambil = models.IntegerField()
    lama_studi = models.IntegerField()
    jalur_masuk = models.CharField(max_length=20)
    tahun_masuk = models.IntegerField()

    def __str__(self):
        return self.nama
