def calculate_total_shipping_fee(distance: float, order_value: int, is_peak_hour: bool, is_raining: bool) -> float:

    if distance <= 0:
        raise ValueError("Distance must be greater than 0")
    if distance > 100:
        raise ValueError("Distance exceeds service limit (100 km)")
    if order_value <= 0:
        raise ValueError("Order value must be greater than 0")
    if distance <= 3:
        base = 0
    else:
        base = distance * 5000

    extra_small_order = 10000 if order_value < 200000 else 0
    extra_peak_hour = 8000 if is_peak_hour else 0
    extra_rain = 12000 if is_raining else 0

    return base + extra_small_order + extra_peak_hour + extra_rain