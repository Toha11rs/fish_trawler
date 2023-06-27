from django.contrib import admin
from django.urls import path
from fish import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main,name='main'),
    path('create_navigations', views.create_navigations, name='create_navigations'),  
    path('delete_navigations/<int:id>/', views.delete_navigations, name='delete_navigations'), 
    path('edit_navigations/<int:pk>/', views.edit_navigations, name='edit_navigations'),
    path('create_trawler', views.add_trawler, name='create_trawler'),  

]


