from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import MahasiswaViewSet, fakultas_distribution, ipk_trend, mahasiswa_per_tahun, organisasi_distribution, ipk_per_fakultas, mahasiswa_summary
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'mahasiswa', MahasiswaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/fakultas-distribution/', fakultas_distribution, name='fakultas-distribution'),
    path('api/ipk-trend/', ipk_trend, name='ipk-trend'),
    path('api/mahasiswa-per-tahun/', mahasiswa_per_tahun, name='mahasiswa-per-tahun'),
    path('api/organisasi-distribution/', organisasi_distribution, name='organisasi-distribution'),
    path('api/ipk-per-fakultas/', ipk_per_fakultas, name='ipk-per-fakultas'),
    path('api/mahasiswa-summary/', mahasiswa_summary, name='mahasiswa-summary'),
    path('', TemplateView.as_view(template_name='index.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)