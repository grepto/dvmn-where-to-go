from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, PlaceImage


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    extra = 0
    model = PlaceImage
    fields = ['image', 'preview_image', 'sort_order']
    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        if not obj.image:
            return format_html('<p>{}</p>', 'Фотография не загружена')

        return format_html('<img src="{url}" height={height}/>',
                           url=obj.image.url,
                           height=min(obj.image.height, 200),
                           )


@admin.register(Place)
class PLaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceImageInline,
    ]
