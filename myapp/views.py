from django.shortcuts import render

# Create your views here.
def hi(request):
    return render(request,'myapp/index.html')