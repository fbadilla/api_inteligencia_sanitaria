from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('CasosEnviados/', views.CasosEnviadosView.as_view(), name='all-CasosEnviados' ),
    path('CasosEnviados/<int:CasosEnviados_id>', views.CasosEnviadosView.as_view(), name='id-CasosEnviados-usr'),
    path('CallCenters/', views.CallCentersView.as_view(), name='all-CallCenters' ),
    path('CallCenters/<int:CallCenters_id>', views.CallCentersView.as_view(), name='id-CallCenters-usr'),
    path('CasosRecibiados/', views.CasosRecibiadosView.as_view(), name='all-CasosRecibiados' ),
    path('CasosRecibiados/<int:CasosRecibiados_id>', views.CasosRecibiadosView.as_view(), name='id-CasosRecibiados-usr'),
    path('CasosComunas/', views.CasosComunasView.as_view(), name='all-CasosComunas' ),
    path('CasosComunas/<int:CasosComunas_id>', views.CasosComunasView.as_view(), name='id-CasosComunas-usr'),
]
