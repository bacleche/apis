from django.contrib import admin
from .models import Webtoon, Episode, Panel, Rating, Bookmark


# Register your models here.
@admin.register(Webtoon)
class WebtoonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'creator',
        'rating',
        'created_at',
    )
    list_filter = ('created_at',)
    search_fields = ('title', 'creator__username')
    ordering = ('-created_at',)
    
    
    
class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1
    fields = ('title', 'order')
    ordering = ('order',)


class PanelInline(admin.TabularInline):
    model = Panel
    extra = 1
    fields = ('image', 'order')
    ordering = ('order',)


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'webtoon',
        'order',
        'created_at',
    )
    list_filter = ('webtoon',)
    search_fields = ('title', 'webtoon__title')
    ordering = ('webtoon', 'order')

    inlines = [PanelInline]



@admin.register(Panel)
class PanelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'episode',
        'order',
        'created_at',
    )
    list_filter = ('episode__webtoon',)
    ordering = ('episode', 'order')



@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'webtoon',
        'score',
        'created_at',
    )
    list_filter = ('score',)
    search_fields = ('user__username', 'webtoon__title')
