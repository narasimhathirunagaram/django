# pricing/views.py
from django.shortcuts import render
from .forms import PricingConfigForm
from .models import PricingConfig
from .utils import calculate_price
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def calculate_pricing(request):
    price = None  # Initialize price variable

    if request.method == 'POST':
        form = PricingConfigForm(request.POST)
        if form.is_valid():
            # Extract input values from the form
            distance = form.cleaned_data['distance']
            time = form.cleaned_data['time']
            wait_time = form.cleaned_data['wait_time']
            day_of_week = form.cleaned_data['day_of_week']

            # Fetch a valid dbp value from an existing instance in the database
            pricing_config = PricingConfig.objects.filter(day_of_week=day_of_week).first()
            if pricing_config:
                dbp = pricing_config.dbp
                print(f"Selected DBP for {day_of_week}: {dbp}")  # Add this line for debugging
            else:
                return render(request, 'error.html', {'message': 'No pricing configuration found for the given day_of_week'})

            # Calculate the price using the provided input values and dbp
            price = calculate_price(dbp, distance, time, wait_time)

    else:
        # If the request method is not POST, render the form
        form = PricingConfigForm()

    return render(request, 'calculate_pricing.html', {'form': form, 'price': price})
