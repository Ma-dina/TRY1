from rest_framework import generics
from .models import Inf
from .serializers import InfSerializer
from rest_framework.permissions import IsAuthenticated

class BookApiDetailList(generics.ListCreateAPIView):
    queryset = Inf.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = InfSerializer

class BookApiDeleteList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inf.objects.all()
    serializer_class = InfSerializer
