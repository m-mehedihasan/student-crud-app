from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'),
 path('home/', views.home, name='home'),
 path('create/', views.create, name='create'),
 path('hide/', views.hide, name='hide'),
 path('save', views.save, name='save'),
 path('update/<int:id>', views.update, name='update'),
 path('delete/<int:id>', views.delete, name='delete'),
 path('save_update', views.save_update, name='save_update'),
 path('reload/', views.reload, name='reload'),
]

