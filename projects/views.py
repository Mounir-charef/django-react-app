from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer
from django.core.exceptions import ObjectDoesNotExist


@api_view(['GET'])
def getProjects(request):
    data = Project.objects.all().order_by('-updated')
    srl = ProjectSerializer(data, many=True)
    return Response(srl.data)


@api_view(['GET'])
def getProject(request, pk):
    try:
        project = Project.objects.get(id=pk)
    except ObjectDoesNotExist:
        # return HttpResponseNotFound()
        return Response({'Error': 'not a valid id'}, status=status.HTTP_404_NOT_FOUND)
    srl = ProjectSerializer(project, many=False)
    return Response(srl.data)


@api_view(['POST'])
def createProject(request):
    srl = ProjectSerializer(data=request.data)
    if srl.is_valid():
        srl.save()
        return Response(status=status.HTTP_201_CREATED)

    return Response(srl.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateProject(request, pk):
    try:
        project = Project.objects.get(id=pk)
    except ObjectDoesNotExist:
        # return HttpResponseNotFound()
        return Response({'Error': 'not a valid id'}, status=status.HTTP_404_NOT_FOUND)
    data = request.data

    srl = ProjectSerializer(instance=project, data=data, many=False)
    if srl.is_valid():
        srl.save()
    return Response(srl.data)


@api_view(['DELETE'])
def deleteProject(request, pk):
    try:
        project = Project.objects.get(id=pk)
    except ObjectDoesNotExist:
        # return HttpResponseNotFound()
        return Response({'Error': 'not a valid id'}, status=status.HTTP_404_NOT_FOUND)
    project.delete()
    return Response('Item deleted')
