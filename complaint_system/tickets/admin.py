
from django.contrib import admin
from .models import Ticket
# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'priority', 'status', 'created_at')
    list_filter = ('status', 'priority', 'created_at')
    search_fields = ('user__username', 'description')
    list_editable = ['status']
    date_hierarchy = 'created_at'
    ordering = ('created_at',)

admin.site.register(Ticket, TicketAdmin)

