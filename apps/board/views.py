# Create your views here.
from rest_framework import viewsets
from .models import Board
from .serailizers import BoardSerializer
class BoardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Board.objects.all()
    serializer_class = BoardSerializer