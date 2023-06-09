"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# from category.views import CategoryListView

# from rest_framework.authtoken.views import obtain_auth_token


schema_view = get_schema_view(
    openapi.Info(
        title="Thich2Hand API",
        default_version="v1",
        description="thich2hand",
        terms_of_service="https://www.thich2hand.com",
        contact=openapi.Contact(email="phudinhtruongk18@gmail.com"),
        license=openapi.License(name="Nike License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('me/', include("user.urls")),
    # # DRF
    # path('search/', include("search.urls")),
    # # CATALOG AND PRODUCT URL
    # path('', CategoryListView.as_view(), name='category'),
    # path('category/', include("category.urls")),
    # path('product/', include("product.urls")),
    # path('comment/', include("comment.urls")),
    # # swagger
    # path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # OAuth
    path("", include("social_django.urls", namespace="social")),
    path("auth/", include("drf_social_oauth2.urls", namespace="drf")),
    # just add
    # path('shopping/', view_current.shopping_center, name='shopping_center'),
    path("", include("store.urls")),
    path("carts/", include("carts.urls")),
    path("", include("taikhoan.urls")),
    path("", include("orders.urls")),
    # path("", include("fakesnakegame.urls")),
    # path('api/', include('api.urls')),
    path("aramtool/", include("toolintro.urls")),
    # path('model_ai/', include('binary_model.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )

# else (production case) will be handled by nginx
