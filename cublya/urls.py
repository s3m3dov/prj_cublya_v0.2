from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("vue/",
        TemplateView.as_view(template_name="application.html"),
        name="app",
    ),

    path('', include(('app.core.urls', 'core'), namespace='core')),
    path('', include(('app.shopping.urls', 'shopping'), namespace='shopping')),
    path('cart/', include(('app.cart.urls', 'cart'), namespace='cart')),
    path('order/', include(('app.order.urls', 'order'), namespace='order')),
    path('customer/', include(('app.customer.urls', 'customer'), namespace='customer')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# {{ request.META.HTTP_REFERER }}
# Get previous page in template (saves just one page)

# all()
# filter()
# exclude()

"""
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