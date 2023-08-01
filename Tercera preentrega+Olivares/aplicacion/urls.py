from django.urls import path, include
from.views import *

urlpatterns = [
    path('',index, name = 'Inicio' ),

    path('piezasCarro/',piezaCarro, name = 'PiezasCarro' ),
    path('profesionales/',profesionales, name = 'profesionales' ),
    path('planes/',planes, name = 'planes' ),
    path('tipoCarro/',tipoCarro, name = 'tipoCarro' ),
    path('autoForm/',autoForm, name = 'autoForm' ),

]
