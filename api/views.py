from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import *
"""
The ContactsView will contain the logic on how to:
 GET, POST, PUT or delete the contacts
"""


class CasosEnviadosView(APIView):
    def get(self, request, CasosEnviados_id=None):
        if CasosEnviados_id is not None:
            todos = CasosEnviados.objects.filter(pk=CasosEnviados_id)
            serializer = CasosEnviadosSerializer(todos, many=True)
            return Response(serializer.data)
        else:
            todos = CasosEnviados.objects.all()
            serializer = CasosEnviadosSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CasosEnviadosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        CasosEnviados.objects.filter(id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, CasosEnviados_id):
        todo = CasosEnviados.objects.get(pk=CasosEnviados_id)
        serializer = CasosEnviadosSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, CasosEnviados_id):
        CasosEnviados.objects.get(pk=CasosEnviados_id).delete()
        message = {
            "msg": "borrado"
        }
        return Response(message, status=status.HTTP_200_OK)

class CallCentersView(APIView):
    def get(self, request, CallCenters_id=None):
        if Enviado_id is not None:
            todos = CallCenters.objects.filter(pk=CallCenters_id)
            serializer = CallCentersSerializer(todos, many=True)
            return Response(serializer.data)
        else:
            todos = CallCenters.objects.all()
            serializer = CasosEnviadosSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CallCentersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        CasosEnviados.objects.filter(id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, CallCenters_id):
        todo = CallCenters.objects.get(pk=CallCenters_id)
        serializer = CallCentersSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, CallCenters):
        CasosEnviados.objects.get(pk=CallCenters_id).delete()
        message = {
            "msg": "borrado"
        }
        return Response(message, status=status.HTTP_200_OK)

class ComunasView(APIView):
    def get(self, request, Comunas_id=None):
        if Enviado_id is not None:
            todos = Comunas.objects.filter(pk=Comunas_id)
            serializer = ComunasSerializer(todos, many=True)
            return Response(serializer.data)
        else:
            todos = Comunas.objects.all()
            serializer = ComunasSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ComunasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        Comunas.objects.filter(id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, Comunas_id):
        todo = Comunas.objects.get(pk=Comunas_id)
        serializer = ComunasSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, Comunas):
        CasosEnviados.objects.get(pk=Comunas_id).delete()
        message = {
            "msg": "borrado"
        }
        return Response(message, status=status.HTTP_200_OK)

class EstadosView(APIView):
    def get(self, request, Estados_id=None):
        if Estados_id is not None:
            todos = Estados.objects.filter(pk=Enviado_id)
            serializer = EstadosSerializer(todos, many=True)
            return Response(serializer.data)
        else:
            todos = Estados.objects.all()
            serializer = EstadosSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = EstadosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        Comunas.objects.filter(id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, Estados_id):
        todo = Comunas.objects.get(pk=Estados_id)
        serializer = ComunasSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, Estados_id):
        CasosEnviados.objects.get(pk=Estados_id).delete()
        message = {
            "msg": "borrado"
        }
        return Response(message, status=status.HTTP_200_OK)

class CasosRecibiadosView(APIView):
    def get(self, request, CasosRecibiados_id=None):
        if CasosRecibiados_id is not None:
            todos = CasosRecibiados.objects.filter(pk=CasosRecibiados_id)
            serializer = CasosRecibiadosSerializer(todos, many=True)
            return Response(serializer.data)
        else:
            todos = CasosRecibiados.objects.all()
            serializer = CasosRecibiadosSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CasosRecibiadosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        CasosRecibiados.objects.filter(id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, CasosRecibiados_id):
        todo = CasosRecibiados.objects.get(pk=CasosRecibiados_id)
        serializer = CasosRecibiadosSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, CasosRecibiados_id):
        CasosRecibiados.objects.get(pk=CasosRecibiados_id).delete()
        message = {
            "msg": "borrado"
        }
        return Response(message, status=status.HTTP_200_OK)

class CasosComunasView(APIView):
    def get(self, request, CasosComunas_id=None):
        if CasosComunas_id is not None:
            todos = CasosComunas.objects.filter(pk=CasosComunas_id)
            serializer = CasosComunasSerializer(todos, many=True)
            return Response(serializer.data)
        else:
            todos = CasosComunas.objects.all()
            serializer = CasosComunasSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CasosComunasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        CasosComunas.objects.filter(id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, CasosComunas_id):
        todo = CasosComunas.objects.get(pk=CasosComunas_id)
        serializer = CasosComunasSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, CasosComunas_id):
        CasosComunas.objects.get(pk=CasosComunas_id).delete()
        message = {
            "msg": "borrado"
        }
        return Response(message, status=status.HTTP_200_OK)

class CasosEstadoView(APIView):
    def get(self, request, CasosEstado_id=None):
        if CasosEstado_id is not None:
            todos = CasosEstado.objects.filter(pk=CasosEstado_id)
            serializer = CasosEstadoSerializer(todos, many=True)
            return Response(serializer.data)
        else:
            todos = CasosEstado.objects.all()
            serializer = CasosEstadoSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CasosEstadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        CasosEstado.objects.filter(id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, CasosEstado_id):
        todo = CasosEstado.objects.get(pk=CasosEstado_id)
        serializer = CasosEstadoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, CasosEstado_id):
        CasosEstado.objects.get(pk=CasosEstado_id).delete()
        message = {
            "msg": "borrado"
        }
        return Response(message, status=status.HTTP_200_OK)
       
class CasosEstadoView(APIView):
    def get(self, request, CasosEstado_id=None):
        if CasosEstado_id is not None:
            todos = CasosEstado.objects.filter(pk=CasosEstado_id)
            serializer = CasosEstadoSerializer(todos, many=True)
            return Response(serializer.data)
        else:
            todos = CasosEstado.objects.all()
            serializer = CasosEstadoSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CasosEstadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        CasosEstado.objects.filter(id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, CasosEstado_id):
        todo = CasosEstado.objects.get(pk=CasosEstado_id)
        serializer = CasosEstadoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, CasosEstado_id):
        CasosEstado.objects.get(pk=CasosEstado_id).delete()
        message = {
            "msg": "borrado"
        }
        return Response(message, status=status.HTTP_200_OK)