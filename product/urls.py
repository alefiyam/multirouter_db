
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'admin/login.html'}),
    url(r'^home/$', views.home, name='home'),
    url('^create-product/$',
        login_required(views.ProductCreate.as_view(), ),
        name='create_product'),
    url('^product_list/$',
        login_required(views.ProductList.as_view(), ),
        name='product_list'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
]
