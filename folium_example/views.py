from django.shortcuts import render
import folium
from .models import EVChargingLocation
from folium.plugins import FastMarkerCluster
from django.db.models import Avg

# Create your views here.
def index(request):
    avg_lat=EVChargingLocation.objects.aggregate(avg=Avg('latitude'))['avg']

    # stations=EVChargingLocation.objects.filter(latitude__gt=avg_lat)
    stations=EVChargingLocation.objects.exclude(latitude__gt=avg_lat)

    m=folium.Map(location=[41.5025,-72.699997],zoom_start=9)
    latitudes=[station.latitude for station in stations]
    longitudes=[station.longitude for station in stations]
        # coordinates=(station.latitude,station.longitude)
        #folium.Marker(coordinates,popup=station.Station_Name).add_to(m)
    FastMarkerCluster(data=list(zip(latitudes,longitudes))).add_to(m)
    context = {'map':m._repr_html_()}
    return render(request, 'index.html', context)

