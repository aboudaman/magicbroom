from django.contrib import admin
from .models import QuotationRequests
# , ServiceType, \
                    # ExtraService, SquareFeet

# Supercharge admin
class MagicAdmin(admin.ModelAdmin):
    fieldsets = [
    # ("Quotation Information", {"fields": ["first_name", "last_name", "telephone"]}),

    ]
    # Set up readonly field in admin
    readonly_fields = ("first_name", "last_name")

    # Set up columns in the list
    list_display = ("first_name", "last_name", "telephone","booking_date", "address")

    # Set ordering format
    list_display_links = ("first_name",)

    # Add a filster
    list_filter = ("telephone",)

    # Add searchable fields
    search_fields = ("telephone", "first_name", "last_name")



# Register your models here.
admin.site.register(QuotationRequests, MagicAdmin)
# admin.site.register(HouseInformation)
# admin.site.register(ServiceType)
# admin.site.register(ExtraService)
# admin.site.register(SquareFeet)
