from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoryForm, ProductForm
from .models import Category, Product

from django.db import models


@login_required
def product_list(request):
    query = request.GET.get("q", "").strip()
    category_id = request.GET.get("category", "").strip()
    status = request.GET.get("status", "").strip()

    products = Product.objects.select_related("category").all()

    if query:
        products = products.filter(
            models.Q(name__icontains=query)
            | models.Q(sku__icontains=query)
            | models.Q(brand__icontains=query)
            | models.Q(model__icontains=query)
        )

    if category_id:
        products = products.filter(category_id=category_id)

    if status == "active":
        products = products.filter(is_active=True)
    elif status == "inactive":
        products = products.filter(is_active=False)

    products = products.order_by("name")

    categories = Category.objects.filter(
        is_active=True
    ).order_by("name")

    return render(
        request,
        "catalog/product_list.html",
        {
            "products": products,
            "categories": categories,
            "query": query,
            "selected_category": category_id,
            "selected_status": status,
        },
    )


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
    query = request.GET.get("q", "").strip()

    categories = Category.objects.all()

    if query:
        categories = categories.filter(
            name__icontains=query
        )

    categories = categories.order_by("name")

    return render(
        request,
        "catalog/category_list.html",
        {
            "categories": categories,
            "query": query,
        },
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
