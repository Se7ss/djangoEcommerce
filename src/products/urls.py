from django.urls import path
from .views import ProductListView, product_list_view, product_detail_view, ProductDetailView, ProductFeaturedListView


urlpatterns = [
    path('productlist/', ProductListView.as_view()),
    path('productfeaturedlist/', ProductFeaturedListView.as_view()),
    path('myproductlist/', product_list_view),
    #path('<int:id>/', product_detail_view, name='product_detail'),

    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail')

]
