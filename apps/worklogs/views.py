from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.worklogs.serializers import WorlogSerializer
from apps.worklogs.models import Worklog

class WorklogView(viewsets.ModelViewSet):
    queryset = Worklog.objects.all()
    serializer_class = WorlogSerializer
    permission_classes = (AllowAny,)
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        worklog_serializer = WorlogSerializer(data=request.data)

        if worklog_serializer.is_valid():
            worklog_serializer.save()
            return Response(worklog_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(worklog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = Worklog.objects.filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        worklog = Worklog.objects.get(pk=kwargs['pk'])
        worklog.is_active = False
        worklog.save()
        return Response(status=status.HTTP_202_ACCEPTED)
