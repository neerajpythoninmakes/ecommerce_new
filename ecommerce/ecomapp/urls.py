from django.conf.urls.static import static

from . import views
from django.conf.urls.static import static
from django.urls import path
app_name='shop'
urlpatterns = [


    path('', views.allprodcat, name='allprodcat'),
    path('<slug:c_slug>/', views.allprodcat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proddetail, name='prodcatdetails'),


]