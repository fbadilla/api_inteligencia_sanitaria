"""
All your application modules and serializers are going to be declared inside this file
"""
from rest_framework import serializers
from django.db import models

"""
Define he Contact Entity into your applcation model
"""
class CasosEnviados(models.Model):
    tipo = models.CharField(max_length=20, default='')
    date = models.DateField(auto_now=False, auto_now_add=False,)
    Cantidad = models.CharField(max_length=30, default='')
"""
The ContactSerializer is where you will specify what properties
from the ever Contact should be inscuded in the JSON response
"""
class CallCenters(models.Model):
    Name_call = models.CharField(max_length=20, default='')
    Description = models.CharField(max_length=50, default='')
    Activo = models.BooleanField(default=True)

class Comunas(models.Model):
    Name_comuna = models.CharField(max_length=20, default='')
    Activo = models.BooleanField(default=True)

class Estados(models.Model):
    Name_estado = models.CharField(max_length=20, default='')
    Activo = models.BooleanField(default=True)

class CasosRecibiados(models.Model):
    tipo = models.CharField(max_length=20, default='')
    date = models.DateField(auto_now=False, auto_now_add=False,)
    Cantidad = models.CharField(max_length=30, default='')
    callcenter = models.ForeignKey(CallCenters,on_delete=models.CASCADE)

class CasosComunas(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False,)
    Cantidad = models.CharField(max_length=30, default='')
    Comuna = models.ForeignKey(Comunas,on_delete=models.CASCADE)

class CasosEstado(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False,)
    Cantidad = models.CharField(max_length=30, default='')
    Comuna = models.ForeignKey(Estados,on_delete=models.CASCADE)

class CasosEnviadosSerializer(serializers.ModelSerializer):

    class Meta:
        model = CasosEnviados
        fields = ('id', 'tipo','date', 'Cantidad')

class CallCentersSerializer(serializers.ModelSerializer):

    class Meta:
        model = CallCenters
        fields = '__all__'

class ComunasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comunas
        fields = '__all__'

class EstadosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estados
        fields = '__all__'

class CasosRecibiadosSerializer(serializers.ModelSerializer):

    class Meta:
        model = CasosRecibiados
        fields = '__all__'

class CasosComunasSerializer(serializers.ModelSerializer):

    class Meta:
        model = CasosComunas
        fields = '__all__'

class CasosEstadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CasosEstado
        fields = '__all__'