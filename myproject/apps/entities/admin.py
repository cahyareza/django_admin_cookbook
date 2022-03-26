from django.contrib import admin
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

    def hero_count(self, obj):
        return obj.hero_set.count()

    def villain_count(self, obj):
        return obj.villain_set.count()