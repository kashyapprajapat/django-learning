from django.contrib import admin
from django.urls import path, include
from . import views  # Import your views here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('expenses/', include('expenses.urls')),  # Include the expenses app URLs
    path('', views.home, name='home'),  # Root URL mapped to a view
]
