from django.urls import path,include
from apps.CORP.corp_empresas.views import(
	empresas_create,
	empresas_list,
	empresas_listOne,
	empresas_update,
	empresas_delete,
	empresas_list_filtro,
	empresas_list_comercial,
	empresas_list_ifis,
	empresas_list_convenio,
	empresas_create_convenio,
	empresas_listOne_filtros,
	empresas_list_logos,
	empresas_list_array,
)
app_name = 'corp_empresas'

urlpatterns = [
	path('create/', empresas_create, name="empresas_create"),
	path('list/', empresas_list, name="empresas_list"),
	path('list/filtro', empresas_list_filtro, name="empresas_list_filtro"),
	path('list/comercial', empresas_list_comercial, name="empresas_list_comercial"),
	path('list/ifis', empresas_list_ifis, name="empresas_list_ifis"),
	path('listOne/<str:pk>', empresas_listOne, name="empresas_listOne"),
	path('update/<str:pk>', empresas_update, name="empresas_update"),
	path('delete/<str:pk>', empresas_delete, name="empresas_delete"),
	path('list/convenio/', empresas_list_convenio, name="empresas_list_convenio"),
	path('create/convenio', empresas_create_convenio, name="empresas_create_convenio"),
	path('listOne/filtros/', empresas_listOne_filtros, name="empresas_listOne_filtros"),
	path('list/logos', empresas_list_logos, name="empresas_list_logos"),
	path('list/empresas/array/', empresas_list_array, name="empresas_list_array"),
]

