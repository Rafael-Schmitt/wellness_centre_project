from django.db import models

class ContactSubmission(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    interest = models.CharField(max_length=100, choices=[
        ('yoga', 'Oceanfront Yoga Retreat'),
        ('spa', 'Rainforest Spa Experience'),
        ('detox', 'Digital Detox Program'),
        ('custom', 'Custom Wellness Journey'),
    ])
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-submitted_at']
        verbose_name_plural = 'Contact Submissions'
    
    def __str__(self):
        return f"Contact from {self.name} - {self.interest}"
