from django.shortcuts import render

def index(request):
    return render(request, 'developer-v1.5/index.html')