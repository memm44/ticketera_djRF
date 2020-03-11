from .models import Issue, Responsible
from .serializers import IssueSerializer, ResponsibleSerializer, UserSerializer
from rest_framework.views import APIView, Response
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated


class ListIssues(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    # def get(self, request):
    #     # obtenemos todos los registros de la BD
    #     issue = Issue.objects.all()
    #     # serializamos la data que recuperamos de la BD
    #     issue_json = IssueSerializer(issue, many=True)
    #     return Response(issue_json.data)
    #
    # def post(self, request):
    #     # serializamos la data y posteriormente verifiamos que esta sea valida.
    #     issue_json = IssueSerializer(data=request.data)
    #     if issue_json.is_valid():
    #         issue_json.save()
    #         return Response(issue_json.data, status=200)
    #     return Response(issue_json.errors, status=400)


class DetailIssue(APIView):
    def get(self, request, pk):
        issue = get_object_or_404(klass=Issue, pk=pk)
        issue_json = IssueSerializer(issue)
        return Response(issue_json.data)

    def put(self, request, pk):
        issue = get_object_or_404(klass=Issue, pk=pk)
        issue_json = IssueSerializer(issue, data=request.data)
        if "id_responsible" in request.data:
            resp = Responsible.objects.filter(id=request.data.get('id_responsible'))
            request.data['id_responsible'] = resp[0]
        if issue_json.is_valid():
            issue_json.save()
            return Response(issue_json.data, status=202)
        return Response(issue_json.errors, status=400)

    def patch(self, request, pk):
        issue = get_object_or_404(klass=Issue, pk=pk)
        issue_json = IssueSerializer(issue, data=request.data, partial=True)
        actual_responsable = issue.id_responsible_id
        # validamos si se envia un campo id_responsible en la petición
        if "id_responsible" in request.data:
            # si se envia el campo lo buscamos en la base de datos con el valor de la petición
            id_recibido = request.data.get('id_responsible')
            resp = Responsible.objects.filter(id=id_recibido)
            # si la logitud es mayor a cero es porque consiguio el usuario y lo remplazaremos
            # de lo contrario guardamos el actual.
            if len(resp) > 0:
                request.data['id_responsible'] = resp[0]
            else:
                request.data['id_responsible'] = actual_responsable
        if issue_json.is_valid():
            issue_json.save()
            return Response(issue_json.data, status=202)
        return Response(issue_json.errors, status=400)

    def delete(self, request, pk):
        issue = get_object_or_404(klass=Issue, pk=pk)
        issue.delete()
        return Response(status=204)


class AsignIssue(APIView):
    def patch(self, request):
        issue = get_object_or_404(klass=Issue, pk=request.data.get('id'))
        actual_responsable = issue.id_responsible_id
        issue_json = IssueSerializer(issue, data=request.data, partial=True)
        # validamos si se envia un campo id_responsible en la petición
        if "id_responsible" in request.data:
            # si se envia el campo lo buscamos en la base de datos con el valor de la petición
            id_recibido = request.data.get('id_responsible')
            resp = Responsible.objects.filter(id=id_recibido)
            # si la logitud es mayor a cero es porque consiguio el usuario y lo remplazaremos
            # de lo contrario guardamos el actual.
            if len(resp) > 0:
                request.data['id_responsible'] = resp[0]
            else:
                request.data['id_responsible'] = actual_responsable
        # armado la data serializada verificamos si esta es valida y la guardamos en la base de datos
        if issue_json.is_valid():
            issue_json.save()
            return Response(issue_json.data, status=202)
        return Response(issue_json.errors, status=400)


class ListResponsible(generics.ListCreateAPIView):
    queryset = Responsible.objects.all()
    serializer_class = ResponsibleSerializer
    # def get(self, request):
    #     # obtenemos todos los registros de la BD
    #     resp = Responsible.objects.all()
    #     # serializamos la data que recuperamos de la BD
    #     resp_json = ResponsibleSerializer(resp, many=True)
    #     return Response(resp_json.data)
    #
    # def post(self, request):
    #     # serializamos la data y posteriormente verifiamos que esta sea valida.
    #     issue_json = ResponsibleSerializer(data=request.data)
    #     if issue_json.is_valid():
    #         issue_json.save()
    #         return Response(issue_json.data, status=200)
    #     return Response(issue_json.errors, status=400)
    #
    # def delete(self, request, pk):
    #     # eliminar registro
    #     resp = get_object_or_404(klass=Responsible, pk=pk)
    #     resp.delete()
    #     return Response(status=204)


class DetailResponsible(generics.RetrieveAPIView):
    # def get(self, request, pk):
    #     resp = get_object_or_404(Responsible, pk=pk)
    #     resp_json = ResponsibleSerializer(resp).data
    #     return Response(resp_json)
    queryset = Responsible.objects.all()
    serializer_class = ResponsibleSerializer


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    # forma manual de devolvver un token
    def post(self, request):
        # guardamos los campos de la peticion en variables
        username = request.data.get('username')
        password = request.data.get('password')
        # usamos la funcion authenticate nativa de django pasandole los campos
        user = authenticate(username=username, password=password)
        # si existe el usuario y el pass esta correcto devuelve su token de lo contrario
        # envia un parametro diciendo error de credenciales
        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error': 'credenciales incorrectas'}, status=400)


class ResponsibleViewSet(viewsets.ModelViewSet):
    queryset = Responsible.objects.all()
    serializer_class = ResponsibleSerializer
    permission_classes = ([IsAuthenticated, IsOwner])
