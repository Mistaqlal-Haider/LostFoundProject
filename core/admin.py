from django.contrib import admin
from .models import Item

# This line creates the table in the admin panel
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'location', 'date_reported')
    list_filter = ('status', 'date_reported')
    search_fields = ('title', 'location')
    # Added 'is_approved' to the list
    list_display = ('title', 'status', 'is_approved', 'date_reported')
    
    # This allows you to check the box directly in the list!
    list_editable = ('is_approved',)
    
    list_filter = ('is_approved', 'status')