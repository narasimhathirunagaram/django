# pricing/forms.py
from django import forms
from .models import PricingConfig

class PricingConfigForm(forms.ModelForm):
    distance = forms.DecimalField()
    time = forms.DecimalField()
    wait_time = forms.DecimalField()
    day_of_week = forms.ChoiceField(
        choices=[
            ('Mon', 'Monday'),
            ('Tue', 'Tuesday'),
            ('Wed', 'Wednesday'),
            ('Thu', 'Thursday'),
            ('Fri', 'Friday'),
            ('Sat', 'Saturday'),
            ('Sun', 'Sunday'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})  # Add any additional attributes you need
    )
    class Meta:
        model = PricingConfig
        fields = ['distance', 'time', 'wait_time']
