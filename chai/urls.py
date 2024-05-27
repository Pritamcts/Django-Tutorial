
from django.urls import path
from .import views

# example
# localhost:8000/chai
# localhost:8000/chai/order/

# {{This is variable}}
# {%this is template%}
urlpatterns = [
    path('', views.jinja_all, name="jinja_all"),
    path('<int:chai_id>/', views.chai_description, name="chai_description"),
]
