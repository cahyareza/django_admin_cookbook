from django.contrib import admin
from django.db.models import Count
from .models import Category, Origin, Hero, Villain
from django.contrib.auth.models import User, Group

# Unregister your models here.
admin.site.unregister(User)
admin.site.unregister(Group)

# Register your models here.
admin.site.register(Category)
# admin.site.register(Hero)
admin.site.register(Villain)

class IsVeryBenevolentFilter(admin.SimpleListFilter):
    title = "is_very_benevolent"
    parameter_name = "is_very_benevolent"

    def lookups(self, request, model_admin):
        return (
            ("Yes", "Yes"),
            ("No", "No"),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == "Yes":
            return queryset.filter(benevolence_factor__gt=75)
        elif value == 'No':
            return queryset.exclude(benevolence_factor__gt=75)
        return queryset


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ("name", "is_immortal", "category", "origin")
    list_filter = ("is_immortal", "category", "origin", IsVeryBenevolentFilter)

    def is_very_benevolent(self, obj):
        return obj.benevolent_factor > 75

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

    hero_count.admin_order_field = "_hero_count"
    villain_count.admin_order_field = "_villain_count"