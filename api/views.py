from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Avg
from .models import Mahasiswa
from .serializers import MahasiswaSerializer
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100

class MahasiswaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer
    pagination_class = StandardResultsSetPagination

@api_view(['GET'])
def fakultas_distribution(request):
    data = Mahasiswa.objects.values('fakultas').annotate(jumlah=Count('nim'))
    return Response(data)

@api_view(['GET'])
def ipk_trend(request):
    data = Mahasiswa.objects.values('semester').annotate(ipk=Avg('ipk')).order_by('semester')
    return Response(data)

@api_view(['GET'])
def mahasiswa_per_tahun(request):
    data = Mahasiswa.objects.values('tahun_masuk').annotate(jumlah=Count('nim')).order_by('tahun_masuk')
    return Response(data)

@api_view(['GET'])
def organisasi_distribution(request):
    data = Mahasiswa.objects.values('organisasi').annotate(jumlah=Count('nim'))
    return Response(data)

@api_view(['GET'])
def ipk_per_fakultas(request):
    data = Mahasiswa.objects.values('fakultas').annotate(ipk_rata_rata=Avg('ipk'))
    return Response(data)

@api_view(['GET'])
def mahasiswa_summary(request):
    total_mahasiswa = Mahasiswa.objects.count()
    average_ipk = Mahasiswa.objects.aggregate(Avg('ipk'))['ipk__avg']
    return Response({
        'total_mahasiswa': total_mahasiswa,
        'average_ipk': average_ipk
    })