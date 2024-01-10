# pricing/utils.py
from decimal import Decimal, ROUND_HALF_UP

def calculate_price(dbp, distance, time, wait_time):
    # Constants for pricing tiers
    dap_threshold = 3  # Additional distance threshold
    dap_rate_1 = 30  # Rate for distance beyond the threshold
    dap_rate_2 = 28  # Different rate for another distance beyond the threshold
    tmf_tier_1 = 1  # Multiplier for time up to 1 hour
    tmf_tier_2 = 1.25  # Multiplier for time beyond 1 hour up to 2 hours
    tmf_tier_3 = 2.2  # Multiplier for time beyond the previous tiers
    wc_rate = 5  # Waiting charges rate per 3 minutes after initial 3 minutes

    # Calculate distance additional price (DAP)
    dap = 0
    if distance > dap_threshold:
        dap = (distance - dap_threshold) * dap_rate_1

    # Calculate time multiplier factor (TMF)
    if time <= 1:
        tmf = tmf_tier_1
    elif 1 < time <= 2:
        tmf = tmf_tier_2
    else:
        tmf = tmf_tier_3

    # Calculate total price
    total_price = (dbp + dap) + (time * Decimal(str(tmf))) + ((wait_time // 3) * wc_rate)
    total_price = total_price.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

    return total_price
