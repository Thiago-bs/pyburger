from django.contrib import admin
from django.urls import path, include
from snackbar import views
from django.views.generic import RedirectView

urlpatterns = [
    path('' , RedirectView.as_view(url='snacks/')),
    path('snacks/', views.snacks),
    path('snacks/more/<int:snack_id>/', views.add_ingredient),
    path('promotions/', views.promotions),
    path('snacks/ingredients/', views.ingredients),
]
