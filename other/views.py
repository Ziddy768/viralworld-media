from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def simple_view(request):
    return render(request, 'templates/simple_view.html')

def mock_view(request):
    return render(request, 'templates/mock1.html')
