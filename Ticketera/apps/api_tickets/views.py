from .models import Issue, Responsible
from .serializers import IssueSerializer, ResponsibleSerializer
from rest_framework.views import APIView, Response
from django.shortcuts import get_object_or_404


class ListIssues(APIView):
    def get(self, request):
        # obtenemos todos los registros de la BD
        issue = Issue.objects.all()
        # serializamos la data que recuperamos de la BD
        issue_json = IssueSerializer(issue, many=True)
        return Response(issue_json.data)

    def post(self, request):
        # serializamos la data y posteriormente verifiamos que esta sea valida.
        issue_json = IssueSerializer(data=request.data)
        if issue_json.is_valid():
            issue_json.save()
            return Response(issue_json.data, status=200)
        return Response(issue_json.errors, status=400)


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


class ListResponsible(APIView):
    def get(self, request):
        # obtenemos todos los registros de la BD
        resp = Responsible.objects.all()
        # serializamos la data que recuperamos de la BD
        resp_json = ResponsibleSerializer(resp, many=True)
        return Response(resp_json.data)

    def post(self, request):
        # serializamos la data y posteriormente verifiamos que esta sea valida.
        issue_json = ResponsibleSerializer(data=request.data)
        if issue_json.is_valid():
            issue_json.save()
            return Response(issue_json.data, status=200)
        return Response(issue_json.errors, status=400)

    def delete(self, request, pk):
        # eliminar registro
        resp = get_object_or_404(klass=Responsible, pk=pk)
        resp.delete()
        return Response(status=204)