from django.urls import path
from .views import BookDetails, BookEdit, BookDelete, BookView

urlpatterns = [
    path('Home', BookView.as_view(), name='home'),
    path('Home/details/<slug>', BookDetails.as_view(), name='details'),
    path('Home/delete/<slug>', BookDelete.as_view(), name='delete'),
    path('Home/edit/<slug>', BookEdit.as_view(), name='edit'),
]