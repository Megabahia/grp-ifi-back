from django.urls import path,include
from .views import(
	pagoProveedores_create,
	pagoProveedores_list,
)
app_name = 'corp_pagoProveedores'

urlpatterns = [
	path('create/', pagoProveedores_create, name="pagoProveedores_create"),
	path('list/', pagoProveedores_list, name="pagoProveedores_list"),
]

