from django.contrib import admin
from .models import Complaint, Comment
from django.utils.html import format_html

class CommentInline(admin.TabularInline):
  
    model = Comment
    extra = 0 
    readonly_fields = ('user', 'text', 'created_at')

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
  
    list_display = ('id', 'title', 'user', 'category', 'short_description', 'status', 'assigned_to', 'created_at')
    list_filter = ('status', 'category', 'assigned_to', 'created_at')
    search_fields = ('title', 'description', 'user__username', 'assigned_to__username')
    inlines = [CommentInline]
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    def changelist_view(self, request, extra_context=None):

        if request.user.is_superuser or request.user.groups.filter(name='Helpdesk Manager').exists():
            self.list_editable = ('status', 'assigned_to')
        else:
            self.list_editable = ('status',)
        return super().changelist_view(request, extra_context)

    @admin.display(description='Description')
    def short_description(self, obj):
        return format_html('<span title="{}">{}</span>', obj.description, obj.description[:50])


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('user', 'complaint', 'text', 'created_at')
    search_fields = ('text', 'user__username', 'complaint__title')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

