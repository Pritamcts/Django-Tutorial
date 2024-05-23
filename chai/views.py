from django.shortcuts import render

# Create your views here.

def jinja_all(request):
     return render(request, "chai/all_jinja.html")