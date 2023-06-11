# General imports
from django.shortcuts import render, get_object_or_404, reverse
from django.http import JsonResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# PDF imports
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm
from reportlab.lib.pagesizes import letter, A4

# Additional for barcodes
from reportlab.graphics.barcode import code39, code128, code93
from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing

# Model imports
from .models import Product, Category, SubCategory # HandlingUnit, HandlingUnitMovement
# from companies.models import Company
# from warehouses.models import Warehouse

# Form imports
# from .forms import ProductForm, CategoryForm, SubCategoryForm

# Function imports
from home.today_calculation import today_calc


# All Products view
@login_required
def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all().order_by("display_name")
    all_categories = Category.objects.all()
    all_subcategories = SubCategory.objects.all()

    def is_ajax(request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    if is_ajax(request):
        category = request.GET.get('category')
        if category is not None:
            subcategories = SubCategory.objects.filter(
                category=category).order_by("display_name").values_list('display_name')
            subcategories_id = SubCategory.objects.filter(
                category=category).order_by("display_name").values_list('id')
            return JsonResponse({
                "subcategories_to_return": list(subcategories),
                "subcategories_id_to_return": list(subcategories_id),
                })

    if request.GET:
        if 'category' and 'subcategory' in request.GET:
            query_filter_category = request.GET['category']
            query_filter_subcategory = request.GET['subcategory']
            if query_filter_subcategory != "":
                queries = Q(
                    category_id=query_filter_category) & Q(
                    subcategory_id=query_filter_subcategory)
                products = products.filter(queries)
            else:
                queries = Q(
                    category__id__icontains=query_filter_category)
                products = products.filter(queries)

        if 'category' in request.GET:
            query_filter_category = request.GET['category']
            if query_filter_category != "":
                queries = Q(
                    category__id__icontains=query_filter_category)
                products = products.filter(queries)
            else:
                Product.objects.all().order_by("display_name")

    context = {
        'products': products,
        'all_categories': all_categories,
        'all_subcategories': all_subcategories,
    }

    return render(request, 'products/products.html', context)
