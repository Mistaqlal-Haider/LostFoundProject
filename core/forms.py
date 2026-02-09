from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        # Include all the fields we created
        fields = ['title', 'description', 'location', 'contact_number', 'status', 'image']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Blue Wallet'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe the item...'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Library or Canteen'}),
            # This styling makes the WhatsApp field look good
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '923001234567'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }