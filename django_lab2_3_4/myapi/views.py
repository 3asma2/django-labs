from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Acc
from rest_framework import viewsets
from .serializers import Intakeserializers,Userseriz
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def deleteusers(request):
    return  Response({'msg':'user deleted'})

def notser(request):
    users=Acc.objects.all()
    request.session['Acc']=users[0].id
    dic={}
    for user in users:
        dic[user.id]={'name':user.intakename}
    request.session['usersworkaround']=dic
    print(request.session['usersworkaround'])
    return HttpResponse('not ser error'+str(request.session['usersworkaround']))


class Intakelist(viewsets.ModelViewSet):
    queryset = Acc.objects.all()
    serializer_class = Intakeserializers

class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userseriz
    permission_classes = [permissions.IsAuthenticated]