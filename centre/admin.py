
from django.contrib import admin
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'interest', 'submitted_at', 'is_read')
    list_filter = ('interest', 'is_read', 'submitted_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('submitted_at',)
    list_editable = ('is_read',)
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'interest')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Metadata', {
            'fields': ('submitted_at', 'is_read'),
            'classes': ('collapse',)
        }),
    )
