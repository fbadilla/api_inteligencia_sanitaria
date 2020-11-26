from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('CasosEnviados/', views.CasosEnviadosView.as_view(), name='all-CasosEnviados' ),
    path('CasosEnviados/<int:CasosEnviados_id>', views.CasosEnviadosView.as_view(), name='id-CasosEnviados-usr'),
    path('CasosEnviados/', views.TodoView.as_view(), name='all-CasosEnviados' ),
    path('CasosEnviados/<int:CasosEnviados_id>', views.TodoView.as_view(), name='id-CasosEnviados-usr'),
    path('CasosEnviados/', views.TodoView.as_view(), name='all-CasosEnviados' ),
    path('CasosEnviados/<int:CasosEnviados_id>', views.TodoView.as_view(), name='id-CasosEnviados-usr'),
    path('CasosEnviados/', views.TodoView.as_view(), name='all-CasosEnviados' ),
    path('CasosEnviados/<int:CasosEnviados_id>', views.TodoView.as_view(), name='id-CasosEnviados-usr'),
]
