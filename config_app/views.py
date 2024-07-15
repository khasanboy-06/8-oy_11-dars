from django.shortcuts import render
from .models import User
from rest_framework.viewsets import ModelViewSet

from .serializers import XarajatlarSerializer
from .permissions import XarajatlarPermission

class XarajatlarView(ModelViewSet):
    serializer_class = XarajatlarSerializer
    permission_classes = [XarajatlarPermission]
    
    def get_queryset(self):
        queryset = User.objects.filter(user_id=self.kwargs['pk'])
        return queryset