from re import search
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Search
from .forms import SearchForm
import folium
from geopy.geocoders import Nominatim


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_instance = form.save()
            address = search_instance.address
            return redirect('/a')
    else:
        form = SearchForm()
        print("DEU ERRADO")
    address = Search.objects.all().last()
    geolocator = Nominatim(user_agent="Mapa")
    location = geolocator.geocode(address)
    # Um if para deletar qualquer endereço errado (strings sem sentido)
    if location:
            lat = location.latitude # type: ignore
            lng = location.longitude # type: ignore
            country = location.address.split(",")[-1].strip() # type: ignore
            return lat, lng, country

    # O mapa principal, inicialização.
    mapa = folium.Map(location=[40.6782258, -8.6017174], zoom_start=3)

    #folium.Marker([lat, lng], tooltip='Click for more', popup=country).add_to(mapa)
    
    # Get HTML Representation of Map Object
    mapa = mapa._repr_html_()
    context={
        'mapa' : mapa,
        'form' : form
    }
    return render(request, 'index.html', context)

# Funcao para a pagina inicial, usa o template base.html
def inicio(request):
    
        mensagem = "Esta é a página de início alternativa."
        context = {
            'mensagem': mensagem,
            }
        return render(request, 'base.html', context)
