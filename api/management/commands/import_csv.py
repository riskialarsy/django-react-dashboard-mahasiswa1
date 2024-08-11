import csv
from django.core.management.base import BaseCommand
from api.models import Mahasiswa
from datetime import datetime

class Command(BaseCommand):
    help = 'Impor data mahasiswa dari CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path ke file CSV')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                Mahasiswa.objects.create(
                    nim=row['nim'],
                    nama=row['nama'],
                    jenis_kelamin=row['jenis_kelamin'],
                    jurusan=row['jurusan'],
                    fakultas=row['fakultas'],
                    ipk=float(row['ipk']),
                    semester=int(row['semester']),
                    organisasi=row['organisasi'],
                    tanggal_lahir=datetime.strptime(row['tanggal_lahir'], '%Y-%m-%d').date(),
                    asal_kota=row['asal_kota'],
                    sks_diambil=int(row['sks_diambil']),
                    lama_studi=int(row['lama_studi']),
                    jalur_masuk=row['jalur_masuk'],
                    tahun_masuk=int(row['tahun_masuk'])
                )
        self.stdout.write(self.style.SUCCESS('Data berhasil diimpor'))