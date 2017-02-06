from django.conf.urls import url
from app1.views import index, login, logout

urlpatterns = [
    url(r'login/', login),
    url(r'logout/',logout),
    url(r'^$',index),

]
