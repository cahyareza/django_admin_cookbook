from django.contrib import admin
from .models import Category, Origin, Hero, Villain
from django.contrib.auth.models import User, Group

# Unregister your models here.
admin.site.unregister(User)
admin.site.unregister(Group)

# Register your models here.
admin.site.register(Category)
admin.site.register(Origin)
admin.site.register(Hero)
admin.site.register(Villain)