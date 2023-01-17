from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from product.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', IndexView.as_view()),
    path('index/', IndexView.as_view(), name='index'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('check-out/', CheckView.as_view(), name='check-out'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('product/<int:pk>', ProductView.as_view(), name='product'),
    path('orders/', include('orders.urls', namespace='orders')),
    path('thank/', ThankView.as_view(), name='thank')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
