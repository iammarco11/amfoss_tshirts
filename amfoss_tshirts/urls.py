from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
from tshirt import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.ProductListView.as_view(),name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^tshirt/',include('tshirt.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)