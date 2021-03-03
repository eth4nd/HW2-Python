def calculate_apr(principal, interest_rate, years):
    for i in range(years):
        total_value = principal*((i+interest_rate)**years)
        total_value = float(total_value)
        output = isinstance(total_value, float)
        if output:
           return total_value
        else:
           return False

calculate_apr(500, .03, 65)
