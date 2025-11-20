from django.shortcuts import render, redirect
from .models import Product, Category
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


def add_product(request):
    try:
        category = Category.objects.first()
        if category:
            Product.objects.create(
                name="Test Product 1",
                category=category,
                price=19.99,
                description="This is a test product created via the view.",
            )
            return HttpResponse("Product added successfully!")
        else:
            return HttpResponse("Error: Please create a Category first to associate the product.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)