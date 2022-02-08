from django.urls import path,include
from  rest_framework import routers
from accounts.models import Acc
from .views import Intakelist,UserList
router = routers.DefaultRouter()
router.register(r'Intake',Intakelist)
router.register(r'myusers',UserList)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]