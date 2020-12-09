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
