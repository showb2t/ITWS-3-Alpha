from django.contrib import admin
from .models import temp_read,water_level,soil_moisture
admin.site.register(temp_read)
admin.site.register(water_level)
admin.site.register(soil_moisture)

