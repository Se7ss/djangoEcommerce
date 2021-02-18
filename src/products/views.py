
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from django.shortcuts import get_object_or_404, render

from .models import Product

# Create your views here.


class ProductFeaturedListView(ListView):

    queryset = Product.objects.filter(featured=True)


class ProductListView(ListView):

    queryset = Product.objects.all()


def product_list_view(request):

    queryset = Product.objects.all()

    context = {


        'object_list': queryset
    }

    return render(request, 'products/product_list_view.html', context)


def product_detail_view(request):

    # queryset = Product.objects.filter(id=id)
    instance = get_object_or_404(Product, pk=id)

    context = {


        'object': instance
    }

    return render(request, 'products/product_detail_view.html', context)


class ProductDetailView(DetailView):

    queryset = Product.objects.all()
    #queryset = get_object_or_404(Product, id=self.kwargs['id'])
    template_name = 'products/product_detail_view.html'
