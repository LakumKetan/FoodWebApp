from django.urls import path
from . import views

app_name = "food"

urlpatterns = [
    path('<int:i_id>/', views.details, name='details'),
    path('', views.index,name='index'),
    path('items/', views.items, name = 'items'),

    path('add/',views.create_item, name='create_item'),

    path('delete/<int:id>/', views.delete_item,name='delete_item')
]
