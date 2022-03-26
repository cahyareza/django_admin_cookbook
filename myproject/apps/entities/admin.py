from django.contrib import admin
from django.db.models import Count
from .models import Category, Origin, Hero, Villain
from django.contrib.auth.models import User, Group

# Unregister your models here.
admin.site.unregister(User)
admin.site.unregister(Group)

# Register your models here.
admin.site.register(Category)
# admin.site.register(Origin)
admin.site.register(Hero)
admin.site.register(Villain)

@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    list_display = ("name", "hero_count", "villain_count")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _hero_count = Count("hero", distinct=True),
            _villain_count = Count("villain", distinct=True),
        )
        return queryset

    def hero_count(self, obj):
        return obj._hero_count

    def villain_count(self, obj):
        return obj._villain_count

    # hero_count.admin_order_field = "_hero_count"
    # villain_count.admin_order_field = "_villain_count"