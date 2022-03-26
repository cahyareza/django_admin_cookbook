from django.contrib import admin
from .models import Category, Origin, Hero, Villain

# Register your models here.
admin.site.register(Category)
admin.site.register(Origin)
admin.site.register(Hero)
admin.site.register(Villain)