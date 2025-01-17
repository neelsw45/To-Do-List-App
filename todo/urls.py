from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('update/<int:pk>',views.update,name='update'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('completed/<int:pk>',views.completed,name='completed'),
    path('restore/<int:pk>',views.restore,name='restore'),
]