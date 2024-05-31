from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomerDetail)
admin.site.register(Ajents)
admin.site.register(Appointment)

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('policy_number', 'name', 'coverage_amount', 'premium', 'term')
    search_fields = ('policy_number', 'name')
    list_filter = ('term',)

@admin.register(PolicyApplication)
class PolicyApplicationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'policy', 'application_date', 'is_approved')
    list_filter = ('is_approved',)