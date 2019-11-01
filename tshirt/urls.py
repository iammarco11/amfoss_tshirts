from django.conf.urls import url 
from django.urls import path
from tshirt import views
app_name = 'tshirt'
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.CartView.as_view(), name='cart'),
]