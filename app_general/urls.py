from django.urls import path 
from app_general import views

urlpatterns = [
    path('', views.Home ,name='Home'),
    path('About',views.About, name="About"),

    path('Products', views.products , name='Products'),
    path('<int:item_id>', views.product , name='Product'),
    path("<int:item_id>/favorite", views.favorite_item, name="favorite_item"),
    path("<int:item_id>/unfavorite", views.unfavorite_item, name="unfavorite_item"),
   
    path('Contact', views.Contact ,name='Contact'),

    path('Blogs', views.Blogs ,name='Blogs'),
    path('<int:blog_id>',views.Blog, name="Blog"),


]
