from django.contrib import admin

# Register your models here.

from .models import Counter, Beer

admin.site.register(Counter)
admin.site.register(Beer)
