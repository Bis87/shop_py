from django.shortcuts import render
from datetime import date
# Create your views here.
def landing(request):
    name = 'Bis'
    current_day = date.today()
    return render(request, 'landing/landing.html', locals())