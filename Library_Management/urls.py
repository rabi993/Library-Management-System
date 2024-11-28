from django.contrib import admin
from django.urls import path, include
from core.views import HomeView, home

from django.conf import settings
from django.conf.urls.static import static
# from . import views
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    # path('home/', home, name='homepage'),
    # path('category/<slug:category_slug>/', home, name='category_wise_book'),
    path('accounts/', include('accounts.urls')),
    path('', include('core.urls')),
    path('transactions/', include('transactions.urls')),
    path('books/', include('books.urls')),
]

# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)