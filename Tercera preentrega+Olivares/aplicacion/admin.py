from django.contrib import admin
from .models import piezaCarro, tipoCarro, profesionales
# Register your models here.

admin.site.register(piezaCarro)
admin.site.register(tipoCarro)
admin.site.register(profesionales)