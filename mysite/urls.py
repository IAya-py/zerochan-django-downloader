from django.conf.urls import url
from django.contrib import admin
from myapp import views
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^download/', views.download, name = "download"),
    url(r'^downloadingImage/', views.downloadingImage, name = "downloading"),
    url(r'^admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)