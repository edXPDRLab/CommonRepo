# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from commonrepo.users.models import User as User

#from .models import Snippet
from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer, UserSerializerV2, UserLiteSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents the users in the system.

    As you can see, the collection of snippet instances owned by a user are
    serialized using a hyperlinked representation.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]

class UserViewSetV2(viewsets.ModelViewSet):
    """
    This endpoint presents the users in the system.

    As you can see, the collection of snippet instances owned by a user are
    serialized using a hyperlinked representation.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializerV2
    permission_classes = [IsOwnerOrReadOnly]

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserLiteSerializer(queryset, many=True)
        return Response(serializer.data)    