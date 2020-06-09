from django.contrib import admin
from django.utils.html import mark_safe, format_html
from adminsortable2.admin import SortableInlineAdminMixin

from .models import Place, PlaceImage


# admin.site.register(Place)
# admin.site.register(PlaceImage)


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    extra = 0
    model = PlaceImage
    verbose_name = 'Фотография'
    verbose_name_plural = 'Фотографии'
    fields = ['image', 'preview_image', 'sort_order']
    readonly_fields = ['preview_image', ]

    def preview_image(self, obj):
        return format_html('<img src="{url}" height={height}/>'.format(
            url=obj.image.url,
            height=obj.image.height if obj.image.height <= 200 else 200,
        )
        )


@admin.register(Place)
class PLaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceImageInline
    ]
