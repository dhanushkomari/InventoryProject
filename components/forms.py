from django import forms
from .models import ComponentCategory, Component
from django.contrib.admin.widgets import AdminDateWidget

class CategoryForm(forms.ModelForm):
    class Meta:
        model = ComponentCategory
        fields = ('name', 'description')
        # widgets = {
        #     'name' : forms.TextInput(attrs={'class':'form-control'}),
        #     # 'image': forms.ImageField(attrs = {'class':'form-control'}),
        #     'description': forms.Textarea(attrs = {'class': 'form-control'}),
        # }

class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = ('name', 'category', 'component_location', 'vendor', 'invoice', 'date_of_order', 'stock', 'price', 'description')
        
        