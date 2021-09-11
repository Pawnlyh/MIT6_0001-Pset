current_savings = 0
r = 0.04
portion_down_payment = 0.25


# get salary input
def get_salary():
    annual_salary = input('Enter your annual salary: ')
    portion_saved = input('Enter the percent of your salary to save, as a decimal: ')
    total_cost = input('Enter the cost of your dream home: ')
    semi_annual_raise = input('Enter the semi_annual raise, as a decimal: ')

    return int(annual_salary), float(portion_saved), int(total_cost), float(semi_annual_raise)


# calculate time to save for the down payment
def calculate_months(annual_salary, portion_saved, total_cost, semi_annual_raise):
    global current_savings
    month = 0
    flag = 0
    monthly_salary = annual_salary/12
    down_payment = portion_down_payment * total_cost

    while current_savings <= down_payment:
        current_savings = current_savings * (1+r/12) + monthly_salary * portion_saved
        month = month + 1
        flag = flag + 1
        if flag == 6:
            monthly_salary = monthly_salary * (1+semi_annual_raise)
            flag = 0

    return month


salary = get_salary()
print('Number of months: ' + str(calculate_months(salary[0], salary[1], salary[2], salary[3])))
