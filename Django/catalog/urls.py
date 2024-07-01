from django.urls import path
from . import views

urlpatterns = [
    path('get/users', views.getUsers, name="get users"),
    path('get/user', views.getUser, name="get user"),
    path('get/labs', views.getLabs, name="get labs"),
    path('get/lab', views.getLabById, name="get lab"),
    path('get/pcs', views.getPcs, name="get pcs"),
    path('get/pc', views.getPc, name="get pc"),
    path('post/user', views.postUser, name="post user"),
    path('post/lab', views.postLab, name="post lab"),
    path('post/pc', views.postPc, name="post pc"),
    path('update/pc', views.updatePc, name="update pc"),
    path('update/lab', views.updateLab, name="update lab"),
    path('delete/pc', views.deletePc, name="delete pc"),
    path('delete/lab', views.deleteLab, name="delete lab")
]