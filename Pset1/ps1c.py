r = 0.04
portion_down_payment = 0.25
semi_annual_raise = 0.07
total_cost = 1000000


# get salary input
def get_salary():
    annual_salary = input('Enter your starting annual salary: ')
    return annual_salary


# noinspection DuplicatedCode
def check_month(annual_salary, portion_saved):
    current_savings = 0
    month = 0
    flag = 0
    monthly_salary = annual_salary/12
    down_payment = portion_down_payment * total_cost

    while current_savings <= down_payment:
        if (down_payment - current_savings) <= 100:
            break

        current_savings = current_savings * (1+r/12) + monthly_salary * portion_saved

        month = month + 1
        flag = flag + 1
        if flag == 6:
            monthly_salary = monthly_salary * (1+semi_annual_raise)
            flag = 0

    return month


def bisection_search(annual_salary):
    step = 0
    portion_saved = 5000
    start = 0
    end = 10000

    if check_month(annual_salary, 1) > 36:
        print('It is not possible to pay the down payment in three years.')
        return step, portion_saved

    while True:
        step = step + 1
        flag = check_month(annual_salary, portion_saved/10000)

        if flag > 36:
            var1 = portion_saved
            portion_saved = (portion_saved + end) / 2
            start = var1
        elif flag < 36:
            var2 = portion_saved
            portion_saved = (portion_saved + start) / 2
            end = var2
        else:
            return step, portion_saved


a_salary = get_salary()
results = bisection_search(int(a_salary))
if results[0] != 0:
    print('Best savings rate: ' + str(results[1]/10000))
    print('Steps in bisection search:' + str(results[0]))
