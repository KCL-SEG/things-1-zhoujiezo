from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def home_view(request):
    html_content = """
    <html>
    <head><title>Things</title></head>
    <body><h1>Things</h1></body>
    </html>
    """
    return HttpResponse(html_content)
