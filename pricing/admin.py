# pricing/admin.py
from django.contrib import admin
from .models import PricingConfig

@admin.register(PricingConfig)
class PricingConfigAdmin(admin.ModelAdmin):
    list_display = ('day_of_week', 'dbp')
