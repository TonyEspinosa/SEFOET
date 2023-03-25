from django.urls import path
from . import views

urlpatterns = [
    path('', views.v_prov, name="u_prov_list"),
    path('new', views.v_prov_new, name="u_prov_new"),
    path('upd/<str:pk_prov>/', views.v_prov_upd, name="u_prov_upd"),
    path('del/<str:pk_prov>/', views.v_prov_del, name="u_prov_del"),
]