from . import views
from django.urls import path


app_name = 'food'
urlpatterns = [
    # /food/
    path('', views.IndexClassView.as_view(), name='index'),
    # path('', views.index, name='index'),                         for def based view
    # /food/1
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    # path('<int:item_id>/', views.detail, name='detail'),         for def based view
    path('item/', views.item, name='item'),
    # add item
    path('add', views.CreateItem.as_view(), name='create_item'),
    # path('add', views.create_item, name='create_item'),          for def based view
    # edit
    path('update/<int:id>/', views.update_item, name='update_item'),
    # delete
    path('delete/<int:id>/', views.delete_item, name='delete_item')
]
