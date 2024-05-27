from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404
# Create your views here.

def jinja_all(request):
     # Handelong data from database
     chais=ChaiVarity.objects.all()
     return render(request, "chai/all_jinja.html",{"chais": chais})

def chai_description(request,chai_id):

     chai=get_object_or_404(ChaiVarity,pk=chai_id)
     return render(request,'chai/chai_description.html', {'chai':chai})