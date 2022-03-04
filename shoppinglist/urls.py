from django.urls import path

from . import views

app_name = 'shoppinglist'
urlpatterns = [
	path('', views.index, name='index'),
	path('add/', views.add_item, name='add'),
	path('delete/<int:pk>/', views.delete_item, name='delete'),
	path('check/<int:pk>/', views.check_item, name='check'),
	path('delete/', views.delete_all, name='delete_all'),
	path('detail/<int:pk>/', views.view_item, name='details'),
	path('edit/<int:pk>/', views.update_item, name='edit'),
]