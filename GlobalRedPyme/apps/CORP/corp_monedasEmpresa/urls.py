from django.urls import path,include
from apps.CORP.corp_monedasEmpresa.views import(
	monedasEmpresa_create,
	monedasEmpresa_list,
)
app_name = 'corp_monedasEmpresa'

urlpatterns = [
	path('create/', monedasEmpresa_create, name="monedasEmpresa_create"),
	path('list/', monedasEmpresa_list, name="monedasEmpresa_list"),
]

