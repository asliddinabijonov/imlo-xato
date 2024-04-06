from django.shortcuts import render, redirect
from .models import *
def index(request):
    search = request.GET.get('search', None)
    if search:
        togriSozlar = Togrisoz.objects.filter(soz=search.lower())
        notogriSozlar = NotogriSoz.objects.filter(soz=search.lower())
        if togriSozlar:
            togriSoz = togriSozlar.first()
            notogriSozlar = NotogriSoz.objects.filter(togrisoz=togriSoz)

            context = {
                'togriSoz': togriSoz,
                'notogriSozlar': notogriSozlar
            }
            return render(request, 'index.html', context=context)
        elif notogriSozlar:
            togriSoz = notogriSozlar.first().togrisoz
            notogriSozlar = NotogriSoz.objects.filter(togrisoz=togriSoz)

            context = {
                'togriSoz': togriSoz,
                'notogriSozlar': notogriSozlar,
            }
            return render(request, 'index.html', context=context)
    else:
        context = {
            'togriSoz': None,
            'notogriSozlar': None
        }
        return render(request, 'index.html', context=context)
    return render(request, 'index.html')
