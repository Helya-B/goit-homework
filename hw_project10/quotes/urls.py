from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='main'),
    path('add_quote', views.add_quote, name='add_quote'),
    path('add_author', views.add_author, name='add_author'),
    path('author_details/<int:author_id>', views.author_details, name='author_details'),
]
