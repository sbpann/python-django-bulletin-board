# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Board
from .serailizers import BoardSerializer
from services import user_service
class BoardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    
    def create(self, request, *args, **kwargs):
        request.data["created_by"] = request.user.id
        request.data.pop("moderators")
       
        return super().create(request, *args, **kwargs) 