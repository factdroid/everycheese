from django.urls import path 

from . import views

app_name = "cheeses"
urlpatterns = [
    path(
        '',
        views.CheeseListView.as_view(),
        name='list'
    ),
]