from django.shortcuts import render, redirect
from .forms import CityForm 
from .services import get_weather
from .models import RecentCity
from django.utils.timezone import now

def index(request):
    weather_data = None
    recent_cities = RecentCity.objects.order_by('-created_at')[:5]

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            api = '7233c3026ab34dd8fcb710c8fc6df533'
            weather_data = get_weather(city, api)

            RecentCity.objects.update_or_create(
                name=city,
                defaults={'created_at': now()}
            )

            recent = RecentCity.objects.order_by('-created_at')
            if recent.count() > 5:
                for city_to_delete in recent[5:]:
                    city_to_delete.delete()
    else:
        form = CityForm()

    return render(request, 'index.html', {
        'form': form,
        'weather': weather_data,
        'recent_cities': recent_cities
    })

def clear_recent(request):
    RecentCity.objects.all().delete()
    return redirect('index')  
