from django.urls import path
from . import views

urlpatterns = [
    path("", views.intro, name="introtool"),
    path('category/<slug:toolcategory_slug>/', views.intro, name='tools_by_category'),
    path('category/<slug:toolcategory_slug>/<slug:tool_slug>/', views.tool_detail, name='tool_detail'),
    path('search/', views.search, name='search'),
    path('submit_tool_review/<int:product_id>/', views.submit_tool_review, name='submit_tool_review'),

]
