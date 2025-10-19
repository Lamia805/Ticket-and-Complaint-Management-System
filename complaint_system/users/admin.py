from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group

admin.site.unregister(User)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_groups')
    list_filter = ('is_staff', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        
        if not request.user.is_superuser and not request.user.groups.filter(name='Helpdesk Manager').exists():
            readonly_fields.extend(['is_staff', 'is_superuser', 'groups', 'user_permissions'])
        
        return readonly_fields

    @admin.display(description='Roles')
    def get_groups(self, obj):
      
        return ", ".join([group.name for group in obj.groups.all()])

