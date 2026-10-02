from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoryForm, ProductForm
from .models import Category, Product


@login_required
def product_list(request):
    products = Product.objects.select_related("category").all()
    return render(request, "catalog/product_list.html", {"products": products})


@login_required
def product_create(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("catalog:product_list")

    return render(request, "catalog/product_form.html", {"form": form})


@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect("catalog:product_list")

    return render(
        request,
        "catalog/product_form.html",
        {"form": form, "product": product},
    )


@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(
        request,
        "catalog/category_list.html",
        {"categories": categories},
    )


@login_required
def category_create(request):
    form = CategoryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("catalog:category_list")

    return render(request, "catalog/category_form.html", {"form": form})

@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
            return redirect("catalog:category_list")
    else:
        form = CategoryForm(instance=category)

    return render(
        request,
        "catalog/category_form.html",
        {
            "form": form,
            "category": category,
        },
    )
