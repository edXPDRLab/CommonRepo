# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers

from commonrepo.users.models import User as User

from commonrepo.elos.models import ELO
from commonrepo.snippets_api.models import Snippet

class UserSerializer(serializers.HyperlinkedModelSerializer):
    elos = serializers.HyperlinkedRelatedField(queryset=ELO.objects.all(), view_name='elos:elos-detail', many=True)
    elos_published = serializers.SerializerMethodField()
    snippets = serializers.HyperlinkedRelatedField(queryset=Snippet.objects.all(), view_name='snippet-detail', many=True)
    
    def get_elos_published(self, obj):
        user = None
        request = self.context.get("request")
        
        if request and hasattr(request, "user"):
            user = request.user
        
        return ELO.objects.filter(author=user).filter(is_public=1).count()   

    class Meta:
        model = User
        fields = ('url', 'username', 'organization', 'phone', 'address', 'language', 'area', 'teaching_category', 'teaching_subject_area', 'elos', 'elos_published', 'snippets', )
