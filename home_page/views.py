from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home_page(request):
    return HttpResponse(loader.get_template('home_page.html').render())