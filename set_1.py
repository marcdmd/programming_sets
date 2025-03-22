#232324 DUNGO, Marc Audryn A.
#ITMGT45 Assignment Set 1

def savings(gross_pay, tax_rate, expenses):
    '''Savings.

    This function calculates the money remaining
        for an employee after taxes and expenses.

    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos

    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''
    taxed_pay = int(gross_pay * (1 - tax_rate)) 
    remaining = taxed_pay - expenses  
    return remaining

def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.

    This function calculates how much material input will be wasted
    after running a certain number of jobs that consume
    a set amount of material.

    Parameters
    ----------
    total_material: int
        the total material available
    material_units: str
        the units used to express a quantity of the material (e.g., "kg", "L", etc.)
    num_jobs: int
        the number of jobs to run
    job_consumption: int
        the amount of material consumed per job

    Returns
    -------
    str
        the amount of remaining material expressed with its unit (e.g., "10kg").
    '''
    remaining_material = total_material - (num_jobs * job_consumption)
    return "{}{}".format(remaining_material, material_units)

def interest(principal, rate, periods):
    '''Interest.

    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.

    To calculate simple interest, simply multiply the principal to the quantity (rate * time).
        Add this amount to the principal to get the final value.

    Round down the final amount.

    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested

    Returns
    -------
    int
        the final value of the investment
    '''
    #interest = p r t
    result = principal + (principal * rate * periods) 
    return int(result)  


