from django.urls import path
from . import views
urlpatterns=[
path("",views.home,name='home'),
# path("register",views.few,name='few'),
# path("logout",views.logout,name='logout')
]