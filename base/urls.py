from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete_task/<str:pk>/', views.deleteTask, name="delete_task"),
    path('create_task/', views.createTask, name="create_task"),
    path('completed_task/', views.completedTask, name="completed_task"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),    
    path('logout/', views.logoutUser, name="logout"),
]