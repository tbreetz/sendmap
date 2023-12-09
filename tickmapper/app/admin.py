from django.contrib import admin
from .models import route, crag, profile, tick

# Register your models here.

admin.site.register(route)
admin.site.register(crag)
admin.site.register(profile)
admin.site.register(tick)
