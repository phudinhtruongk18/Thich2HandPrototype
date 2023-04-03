from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from django.db.models import Q

from .models import Product, ReviewRating
from category.models import Category
from django.db.models import Q
from django.contrib import messages
from .forms import ReviewForm
from carts.views import _cart_id
from orders.models import OrderProduct
from carts.models import Cart,CartItem


# Create your views here.
def store(request, category_slug=None):
    messages.info(request, str(category_slug) + "a")

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=categories, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')

    page = request.GET.get('page')
    page = page or 1
    panigator = Paginator(products, 3)
    paged_products = panigator.get_page(page)
    products_count = products.count()

    links = Category.objects.all()

    context = {
        'links': links,
        'products': paged_products,
        'products_count': products_count,
   }
    return render(request, 'store/store.html', context=context)


def product_detail(request, category_slug=None, product_slug=None):

    single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)

    # if that user orders this product so -> is_ordered
    try:
        if request.user.is_authenticated:
            in_cart = CartItem.objects.filter(user=request.user, is_active=True).exists()
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request=request))
            in_cart = CartItem.objects.filter(cart=cart, is_active=True).exists()
    except Exception as e:
        print("---> Cant in_cart in product detail :", e)

    # if that user orders this product so -> is_ordered
    try:
        is_ordered_product = OrderProduct.objects.filter(user=request.user, product_id=single_product.id).exists()
    except Exception:
        is_ordered_product = None

    reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)

    context = {
        'single_product': single_product,
        'in_cart': in_cart if 'in_cart' in locals() else False,
        'is_ordered_product': is_ordered_product,
        'reviews': reviews,
    }
    return render(request, 'store/product_detail.html', context=context)


def search(request):
    if 'q' in request.GET:
        q = request.GET.get('q')
        products = Product.objects.order_by('-created_date').filter(
            Q(product_name__icontains=q) | Q(description__icontains=q))
        products_count = products.count()
    context = {
        'products': products,
        'q': q,
        'products_count': products_count,
    }
    return render(request, 'store/store.html', context=context)


def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            review = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=review)
            form.save()
            messages.success(request, "Thanks for the updating review!")
            return redirect(url)
        except Exception as e:
            print(e)
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, "Thanks for the review!")
                return redirect(url)
