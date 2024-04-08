from rest_framework import serializers
from django.utils.translation import gettext as _

from core.models import Recipe


class ReceipeSerializer(serializers.ModelSerializer):

    class Meta :
        model = Recipe
        fields=['id','title','time','price','link']
        read_only_fields=['id']