from django.contrib import admin
from .models import CasosEnviados , CallCenters ,Comunas , Estados, CasosRecibiados, CasosComunas, CasosEstado
admin.site.register(CasosEnviados)
admin.site.register(CallCenters)
admin.site.register(Comunas)
admin.site.register(Estados)
admin.site.register(CasosRecibiados)
admin.site.register(CasosComunas)
admin.site.register(CasosEstado)