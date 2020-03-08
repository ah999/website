from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    #/music/
    path('' , views.IndexView.as_view(), name='index'),

    #/music/register/
    path('register/', views.UserFormView.as_view(), name='register'),

    #/music/2/
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),

    #/music/2/add/
    path('album/add/', views.ALbumCreate.as_view(), name='album-add'),

    #/music/2/
    path('album/<int:pk>/', views.ALbumUpdate.as_view(), name='album-update'),

    #/music/2/delete/
    path('album/<int:pk>/delete/', views.ALbumDelete.as_view(), name='album-delete'),
]

