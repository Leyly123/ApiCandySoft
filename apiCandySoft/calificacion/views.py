from rest_framework import generics
from .models import Calificacion
from .serializers import CalificacionSerializer

class CalificacionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer
