from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index' ),
    path('new/',views.new,name='new' ),
    path('blog/<pk>/',views.bloger,name='bloger'),
    path('link/',views.link,name='link' ),
	path('add/',views.add,name='add' ),
	path('redirect/<id>/',views.send,name='send'),
	path('register/',views.register,name='register'),
	path('stats/',views.stats,name='stats'),
	path('view_products/',views.view_products,name='view_products'),
	path('view_products/<pk>/',views.give_detail,name='detail'),
	path('view_products/<pk>/call/',views.call,name='call'),
	path('new_add/',views.new_add,name='new_add'),
]
