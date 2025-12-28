from django.contrib import admin
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from .models import ContactSubmission, Customer, Category, Product, Order, OrderItem, User

# Optional: Custom Admin Site
class CustomAdminSite(admin.AdminSite):
    def index(self, request, extra_context=None):
        """
        Add statistics to admin index page
        """
        if extra_context is None:
            extra_context = {}
        
        # Get statistics for the last 7 days
        today = timezone.now()
        week_ago = today - timedelta(days=7)
        
        # Contact submission statistics
        total_submissions = ContactSubmission.objects.count()
        unread_submissions = ContactSubmission.objects.filter(is_read=False).count()
        recent_submissions = ContactSubmission.objects.filter(submitted_at__gte=week_ago).count()
        
        # Interest breakdown
        interest_stats = ContactSubmission.objects.values('interest').annotate(
            count=Count('interest')
        ).order_by('-count')
        
        extra_context.update({
            'total_submissions': total_submissions,
            'unread_submissions': unread_submissions,
            'recent_submissions': recent_submissions,
            'interest_stats': interest_stats,
        })
        
        return super().index(request, extra_context)

# Register your models
@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'interest', 'submitted_at', 'is_read')
    list_filter = ('is_read', 'interest', 'submitted_at')
    search_fields = ('name', 'email', 'message')
    date_hierarchy = 'submitted_at'
    list_per_page = 20
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected submissions as read"
    
    actions = [mark_as_read]

# Register other models
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)

# Optional: To use custom admin site, replace the default admin.site
# custom_admin_site = CustomAdminSite(name='custom_admin')