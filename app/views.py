from .models import ToDo
from app.serializers import TodoSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class TodoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]