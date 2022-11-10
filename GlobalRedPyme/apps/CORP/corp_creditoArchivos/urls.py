from django.urls import path, include
from .views import (
    creditoArchivos_create,
    creditoArchivos_list,
    creditoArchivos_delete,
    uploadEXCEL_creditosPreaprobados,
    uploadEXCEL_microCreditosPreaprobados,
    uploadEXCEL_creditosPreaprobados_empleados,
    creditoArchivos_subir_documentosFirmados_create,
    creditoArchivos_ver_documentosFirmados_list,
)

app_name = 'corp_creditoArchivos'

urlpatterns = [
    path('create/', creditoArchivos_create, name="creditoArchivos_create"),
    path('list/', creditoArchivos_list, name="creditoArchivos_list"),
    path('delete/<int:pk>', creditoArchivos_delete, name="creditoArchivos_delete"),
    path('upload/creditos/preaprobados/<int:pk>', uploadEXCEL_creditosPreaprobados,
         name="uploadEXCEL_creditosPreaprobados"),
    path('upload/microcreditos/preaprobados/<int:pk>', uploadEXCEL_microCreditosPreaprobados,
         name="uploadEXCEL_creditosPreaprobados"),
    path('upload/creditos/preaprobados/empleados/<int:pk>', uploadEXCEL_creditosPreaprobados_empleados,
         name="uploadEXCEL_creditosPreaprobados_empleados"),
    path('subir/documentosFirmados/', creditoArchivos_subir_documentosFirmados_create,
         name="creditoArchivos_subir_documentosFirmados_create"),
    path('documentosFirmados/listar/', creditoArchivos_ver_documentosFirmados_list,
         name="creditoArchivos_ver_documentosFirmados_list"),
]
