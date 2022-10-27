from django.urls import path, include
from .views import (
    creditoPersonas_create,
    creditoPersonas_listOne,
    creditoPersonas_update,
    creditoPersonas_delete,
    creditoPersonas_list,
    uploadEXCEL_creditosPreaprobados,
    uploadEXCEL_creditosPreaprobados_empleados,
    creditoPersonas_listOne_persona,
    creditoPersonas_lecturaArchivos,
    creditoPersonas_creditoPreaprobado_codigo,
    prueba,
)

app_name = 'corp_creditoPersonas'

urlpatterns = [
    path('create/', creditoPersonas_create, name="creditoPersonas_create"),
    path('list/', creditoPersonas_list, name="creditoPersonas_list"),
    path('listOne/<str:pk>', creditoPersonas_listOne, name="creditoPersonas_listOne"),
    path('update/<str:pk>', creditoPersonas_update, name="creditoPersonas_update"),
    path('delete/<str:pk>', creditoPersonas_delete, name="creditoPersonas_delete"),
    path('upload/creditos/preaprobados/', uploadEXCEL_creditosPreaprobados, name="uploadEXCEL_creditosPreaprobados"),
    path('upload/creditos/preaprobados/empleados/', uploadEXCEL_creditosPreaprobados_empleados,
         name="uploadEXCEL_creditosPreaprobados_empleados"),
    path('listOne/persona/<str:pk>', creditoPersonas_listOne_persona, name="creditoPersonas_listOne_persona"),
    path('lecturaArchivos/<str:pk>', creditoPersonas_lecturaArchivos, name="creditoPersonas_lecturaArchivos"),
    path('creditoPreaprobado/codigo', creditoPersonas_creditoPreaprobado_codigo,
         name="creditoPersonas_creditoPreaprobado_codigo"),
    path('prueba', prueba, name="prueba"),
]
