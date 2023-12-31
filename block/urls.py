
from django import views
from django.urls import path
from block.views import home
from block.views import navbar
from block.views import login
from block.views import blog
from block.views import add
from block.views import addrec
from block.views import delete
from block.views import update
from block.views import uprec


urlpatterns = [
    path('home/', home, name="home"),
    path('navbar/', navbar, name="navbar"),
    path('login/',login,name="login"),
    path('blog/', blog ,name="blog"),
    path('add/',add,name="add"),
    path('addrec/',addrec,name="addrec"),
    path('delete/<int:id>/',delete,name="delete"),
    path('update/<int:id>/',update,name="update"),
    path('update/uprec/<int:id>/',uprec,name="uprec"),
]
