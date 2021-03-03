def calculate_apr(principal, interest_rate, years):
    if interest_rate < 0:
       for i in range(years):
           total_value = (principal)*((1+interest_rate)**years)
           total_value = float(total_value)
           output = isinstance(total_value, float)
                  if output:
                     return total_value
                  else:
                     return False
       return total_value

calculate_apr(500, .03, 65)
