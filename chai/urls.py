
from django.urls import path
from .import views

# example
# localhost:8000/chai
# localhost:8000/chai/order/
urlpatterns = [
    path('', views.jinja_all, name="jinja_all"),
]
