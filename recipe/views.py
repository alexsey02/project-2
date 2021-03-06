from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from core.models import Tag
from recipe import serializers
from rest_framework.permissions import IsAuthenticated

class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    queryset=Tag.objects.all()
    serializer_class=serializers.TagSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')
    
    def perform_create(self, serizalizer):
        serizalizer.save(user=self.request.user)

