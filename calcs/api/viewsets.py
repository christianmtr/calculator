from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from calcs.api.serializers import OperationSerializers, RecordSerializers

from calcs.models import Operation, Record


class OperationViewSets(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializers    


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializers


@api_view(['POST'])
def operations(request):
    return Response()
