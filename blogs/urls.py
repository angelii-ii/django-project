from django.urls import path

from blogs import views

urlpatterns=[
    path('',views.index,name='starting_page'),
    path('all_posts',views.all_posts,name='all_posts'),
    path('post/<slug:slug>', views.single_post, name='page_detail'),
    path('product',views.product_list),
    path('<slug:slug>',views.product_detail),
]