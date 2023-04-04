from django.contrib import messages
# Create your views here.
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ToolReviewForm
from .models import Tool, ToolCategory, ToolReviewRating


def intro(response, toolcategory_slug=None):

    if toolcategory_slug is not None:
        categories = get_object_or_404(ToolCategory, slug=toolcategory_slug)
        tools = Tool.objects.all().filter(category=categories, is_available=True)
    else:
        tools = Tool.objects.all().filter(is_available=True).order_by("id")

    categories = ToolCategory.objects.all()

    context = {
        "tools": tools,
        "categories": categories,
    }
    return render(response, "aramtool/overview.html", context=context)


def tool_detail(response, toolcategory_slug=None, tool_slug=None):

    tool = Tool.objects.get(category__slug=toolcategory_slug, slug=tool_slug)

    reviews = ToolReviewRating.objects.filter(product_id=tool.id, status=True)

    context = {
        "tool": tool,
        "reviews": reviews,
    }
    return render(response, "aramtool/tool_detail.html", context=context)


def submit_tool_review(request, product_id):
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        try:
            review = ToolReviewRating.objects.get(
                user__id=request.user.id, product__id=product_id
            )
            form = ToolReviewForm(request.POST, instance=review)
            form.save()
            messages.success(request, "Thanks for the updating review!")
            return redirect(url)
        except Exception as e:
            print(e)
            form = ToolReviewForm(request.POST)
            if form.is_valid():
                data = ToolReviewRating()
                data.subject = form.cleaned_data["subject"]
                data.rating = form.cleaned_data["rating"]
                data.review = form.cleaned_data["review"]
                data.ip = request.META.get("REMOTE_ADDR")
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, "Thanks for the review!")
                return redirect(url)


def search(request):
    if "q" in request.GET:
        q = request.GET.get("q")
        products = Tool.objects.order_by("-created_date").filter(
            Q(product_name__icontains=q) | Q(description__icontains=q)
        )
    context = {
        "products": products,
        "q": q,
    }
    return render(request, "aramtool/overview.html", context=context)
