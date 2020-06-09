from django.shortcuts import render

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
                'detailsUrl': ''
            }
        }
        for place in Place.objects.all()
    ]

    places_geojson = dict(type='FeatureCollection', features=features)
    data = dict(places_geojson=places_geojson)
    return render(request, 'index.html', context=data)
