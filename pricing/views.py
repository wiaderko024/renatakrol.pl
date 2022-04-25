from django.shortcuts import render
from .models import Price


def pricing_page(request):
    prices = Price.objects.all()
    return render(request, 'pricing.html', {'prices': prices})
