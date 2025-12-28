from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model for authentication
class User(AbstractUser):
    # Remove the contact fields from User
    # These will go to a separate ContactSubmission model
    pass

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_level = models.CharField(max_length=50, default='Basic')
    
    def __str__(self):
        return self.user.username

# Separate model for contact form submissions
class ContactSubmission(models.Model):
    INTEREST_CHOICES = [
        ('yoga', 'Oceanfront Yoga Retreat'),
        ('spa', 'Rainforest Spa Experience'),
        ('detox', 'Digital Detox Program'),
        ('custom', 'Custom Wellness Journey'),
    ]
    
    name = models.CharField(max_length=200)
    email = models.EmailField()
    interest = models.CharField(max_length=100, choices=INTEREST_CHOICES)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-submitted_at']
        verbose_name_plural = 'Contact Submissions'
    
    def __str__(self):
        return f"Contact from {self.name} - {self.interest}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    in_stock = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')
    
    def __str__(self):
        return f"Order {self.id} - {self.customer}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}" 