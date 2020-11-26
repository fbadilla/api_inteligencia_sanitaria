from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import CasosEnviados, CasosEnviadosSerializer ,
CallCenters , CallCentersSerializer

"""
The ContactsView will contain the logic on how to:
 GET, POST, PUT or delete the contacts
"""


class CasosEnviadosView(APIView):
    def get(self, request, Enviado_id=None):
        if Enviado_id is not None:
            todos = CasosEnviados.objects.filter(pk=Enviado_id)
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

    def put(self, request, Enviado_id):
        todo = CasosEnviados.objects.get(pk=Enviado_id)
        serializer = CasosEnviadosSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, Enviado_id):
        CasosEnviados.objects.get(pk=Enviado_id).delete()
        message = {
            "msg": "borrado"
        }
        return Response(message, status=status.HTTP_200_OK)

class CallCentersView(APIView):
    def get(self, request, CallCenters_id=None):
        if Enviado_id is not None:
            todos = CallCenters.objects.filter(pk=Enviado_id)
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

class CallCentersView(APIView):
    def get(self, request, CallCenters_id=None):
        if Enviado_id is not None:
            todos = CallCenters.objects.filter(pk=Enviado_id)
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
