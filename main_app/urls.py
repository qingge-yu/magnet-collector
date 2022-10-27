from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('magnets/', views.magnets_index, name='index'),
    path('magnets/<int:magnet_id>/', views.magnets_detail, name='detail'),
    path('magnets/create/', views.MagnetCreate.as_view(), name='magnets_create'),
    path('magnets/<int:pk>/update/',
         views.MagnetUpdate.as_view(), name='magnets_update'),
    path('magnets/<int:pk>/delete/',
         views.MagnetDelete.as_view(), name='magnets_delete'),
    path('magnets/<int:magnet_id>/add_review/',
         views.add_review, name='add_review'),
    path('looks/', views.LookList.as_view(), name='looks_index'),
    path('looks/<int:pk>/', views.LookDetail.as_view(), name='looks_detail'),
    path('looks/create/', views.LookCreate.as_view(), name='looks_create'),
    path('looks/<int:pk>/update', views.LookUpdate.as_view(), name='looks_update'),
    path('looks/<int:pk>/delete', views.LookDelete.as_view(), name='looks_delete'),
    path('magnets/<int:magnet_id>/assoc_look/<int:look_id>/',
         views.assoc_look, name='assoc_look')
]
