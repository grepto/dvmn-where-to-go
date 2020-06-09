import json

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from places.models import Place


def show_main_page(request):
    features = [
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude]
            },
            'properties': {
                'title': place.title,
                'placeId': place.pk,
                'detailsUrl': f'/places/{place.pk}'
            }
        }
        for place in Place.objects.all()
    ]

    places_geojson = dict(type='FeatureCollection', features=features)
    data = dict(places_geojson=places_geojson)
    return render(request, 'index.html', context=data)


def place_detailed_view(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    data = dict(
        title=place.title,
        imgs=[img.image.url for img in place.images.all()],
        description_short=place.description_short,
        description_long=place.description_long,
        coordinates=dict(
            lng=place.longitude,
            lat=place.latitude
        )
    )

    # return JsonResponse(data)
    return JsonResponse(data, json_dumps_params={'indent': 2, 'ensure_ascii': False})
