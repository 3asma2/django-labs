from rest_framework import serializers
from accounts.models import Acc
from django.contrib.auth.models import User
class Intakeserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Acc
        fields=['id','name']

class Userseriz(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=['username','password']