from django.db import models

class Item(models.Model):
    STATUS_CHOICES = [
        ('LOST', 'Lost'),
        ('FOUND', 'Found'),
        ('RETURNED', 'Returned'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200)
    date_reported = models.DateTimeField(auto_now_add=True)
    
    # We increased max_length to 20 to fit 'RETURNED'
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='LOST')
    
    # This is the field that was missing!
    contact_number = models.CharField(max_length=15, help_text="e.g., 923001234567")
    
    image = models.ImageField(upload_to='items_images/', blank=True, null=True)
    
    # This is for the Admin Approval feature
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title