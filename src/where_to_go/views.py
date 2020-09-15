from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def show_main_page(request):
    features = [
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude],
            },
            'properties': {
                'title': place.title,
                'placeId': place.pk,
                'detailsUrl': reverse('place', args=[place.pk]),
            },
        }
        for place in Place.objects.all()
    ]

    places_geojson = {
        'type': 'FeatureCollection',
        'features': features
    }
    data = {'places_geojson': places_geojson}
    return render(request, 'index.html', context=data)


def place_detailed_view(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    data = {
        'title': place.title,
        'imgs': [img.image.url for img in place.images.all()],
        'short_description': place.short_description,
        'long_description': place.long_description,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude,
        },
    }

    return JsonResponse(data, json_dumps_params={'indent': 2, 'ensure_ascii': False})
