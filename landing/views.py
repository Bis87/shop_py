from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SubscriberForm
from datetime import datetime


# Create your views here.
def landing(request):
    form = SubscriberForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        new_form = form.save()
        return HttpResponseRedirect(reverse("landing"))
    else:
        form = SubscriberForm()
    current_day = datetime.now()
    return render(request, 'landing/landing.html', locals())