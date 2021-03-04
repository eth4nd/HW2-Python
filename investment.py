def calculate_apr(principal, interest_rate, years):
    """
    Calculates how much money to make on an investment. 
    """

    #Condtion in place, just in case interest is a negative number. 
    if interest_rate < 0:
       return False
    else:
       #Loops through the amount of years to find the total value. 
       for i in range(years):
           total_value = (principal)*((1+interest_rate)**years)
           total_value = float(total_value)
       return total_value
#To test the condtions, setting 500, 0.03, and 65 to respective parameters.  
calculate_apr(500, .03, 65)
