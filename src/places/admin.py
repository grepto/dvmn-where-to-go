from django.contrib import admin
from .models import Place, PlaceImage

# admin.site.register(Place)
# admin.site.register(PlaceImage)


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    verbose_name = 'Фотография'
    verbose_name_plural = 'Фотографии'


@admin.register(Place)
class PLaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceImageInline
    ]
