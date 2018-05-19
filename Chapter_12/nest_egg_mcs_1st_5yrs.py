"""Retirement nest egg calculator using Monte Carlo simulation."""
import sys
import random
import matplotlib.pyplot as plt

def read_to_list(file_name):
    """Open a file of data in percent, convert to decimal & return a list."""
    with open(file_name) as in_file:
        lines = [float(line.strip()) for line in in_file]
        decimal = [round(line / 100, 5) for line in lines]
        return decimal

def default_input(prompt, default=None):
    """Allow use of default values in input"""
    prompt = '{} [{}]: '.format(prompt, default)
    response = input(prompt)
    if not response and default:
        return default
    else:
        return response

# load data files with original data in percent form
print("\nNote: Input data should be in percent, not decimal!\n")
try:
    bonds = read_to_list('10-yr_TBond_returns_1926-2013_pct.txt')
    stocks = read_to_list('SP500_returns_1926-2013_pct.txt')
    blend_40_50_10 = read_to_list('S-B-C_blend_1926-2013_pct.txt')
    blend_50_50 = read_to_list('S-B_blend_1926-2013_pct.txt')
    infl_rate = read_to_list('annual_infl_rate_1926-2013_pct.txt')
except IOError as e:
    print("{}. \nTerminating program.".format(e), file=sys.stderr)
    sys.exit(1)

# get user input; use dictionary for investment-type arguments   
investment_type_args = {'bonds': bonds, 'stocks': stocks,
                        'sb_blend': blend_50_50, 'sbc_blend': blend_40_50_10}

# print input legend for user
print("   stocks = SP500")
print("    bonds = 10-yr Treasury Bond")
print(" sb_blend = 50% SP500/50% TBond")
print("sbc_blend = 40% SP500/50% TBond/10% Cash\n")

print("Press ENTER to take default value shown in [brackets]. \n")

# get user input
invest_type = default_input("Enter investment type: (stocks, bonds, sb_blend,"\
                     " sbc_blend): \n", 'bonds').lower()
while invest_type not in investment_type_args:
    invest_type = input("Invalid investment. Enter investment type " \
                    "as listed in prompt: ")

start_value = default_input("Input starting value of investments: \n", \
                             '2000000')
while not start_value.isdigit():
    start_value = input("Invalid input! Input integer only: ")

withdrawal_1 = default_input("Input annual pre-tax withdrawal for " \
                            "first 5 yrs(today's $): \n", '100000')
while not withdrawal_1.isdigit():
    withdrawal_1 = input("Invalid input! Input integer only: ")

withdrawal_2 = default_input("Input annual pre-tax withdrawal for " \
                            "remainder (today's $): \n", '80000')
while not withdrawal_2.isdigit():
    withdrawal_2 = input("Invalid input! Input integer only: ")

min_years = default_input("Input minimum years in retirement: \n", '18')
while not min_years.isdigit():
    min_years = input("Invalid input! Input integer only: ")

most_likely_years = default_input("Input most-likely years in retirement: \n",
                                  '25')
while not most_likely_years.isdigit():
    most_likely_years = input("Invalid input! Input integer only: ")

max_years = default_input("Input maximum years in retirement: \n", '40')
while not max_years.isdigit():
    max_years = input("Invalid input! Input integer only: ")
    
num_cases = default_input("Input number of cases to run: \n", '50000')
while not num_cases.isdigit():
    num_cases = input("Invalid input! Input integer only: ")

# check for other erroneous input
if not int(min_years) < int(most_likely_years) < int(max_years) \
   or int(max_years) > 99:
    print("\nProblem with input years.", file=sys.stderr)
    print("Requires Min < ML < Max & Max <= 99.", file=sys.stderr)
    sys.exit(1)
   
def montecarlo(returns):
    """Run MCS & return investment value at death & and # of times bankrupt."""
    case_count = 0
    bankrupt_count = 0
    outcome = []

    while case_count < int(num_cases):
        investments = int(start_value)
        start_year = random.randrange(0, len(returns))        
        duration = int(random.triangular(int(min_years), int(max_years),
                                         int(most_likely_years)))       
        end_year = start_year + duration 
        lifespan = [i for i in range(start_year, end_year)]
        bankrupt = 'no'

        # build temporary lists for each case
        lifespan_returns = []
        lifespan_infl = []
        for i in lifespan:
            lifespan_returns.append(returns[i % len(returns)])
            lifespan_infl.append(infl_rate[i % len(infl_rate)])
            
        # loop through each year of retirement for each case run
        for index, i in enumerate(lifespan_returns):
            infl = lifespan_infl[index]

            # don't adjust for inflation the first year
            if index == 0:
                withdraw_infl_adj_1 = int(withdrawal_1)
                withdraw_infl_adj_2 = int(withdrawal_2)
            else:
                withdraw_infl_adj_1 = int(withdraw_infl_adj_1 * (1 + infl))
                withdraw_infl_adj_2 = int(withdraw_infl_adj_2 * (1 + infl))

            if index < 5:
                withdraw_infl_adj = withdraw_infl_adj_1
            else:
                withdraw_infl_adj = withdraw_infl_adj_2

            investments -= withdraw_infl_adj
            investments = int(investments * (1 + i))

            if investments <= 0:
                bankrupt = 'yes'
                break

        if bankrupt == 'yes':
            outcome.append(0)
            bankrupt_count += 1
        else:
            outcome.append(investments)
            
        case_count += 1

    return outcome, bankrupt_count

def bankrupt_prob(outcome, bankrupt_count):
    """Calculate & return chance of running out of money & print statistics."""
    total = len(outcome)
    odds = round(100 * bankrupt_count / total, 1)

    print("\nInvestment type: {}".format(invest_type))
    print("Starting value: ${:,}".format(int(start_value)))
    print("Annual withdrawal first 5 yrs: ${:,}".format(int(withdrawal_1)))
    print("Annual withdrawal after 5 yrs: ${:,}".format(int(withdrawal_2))) 
    print("Years in retirement (min-ml-max): {}-{}-{}"
          .format(min_years, most_likely_years, max_years))
    print("Number of runs: {:,}\n".format(len(outcome)))
    print("Odds of running out of money: {}%\n".format(odds))
    print("Average outcome: ${:,}".format(int(sum(outcome) / total)))
    print("Minimum outcome: ${:,}".format(min(i for i in outcome)))
    print("Maximum outcome: ${:,}".format(max(i for i in outcome)))

    return odds

def main():
    """Run the program and draw bar chart of results."""    
    outcome, bankrupt_count = montecarlo(investment_type_args[invest_type])
    odds = bankrupt_prob(outcome, bankrupt_count)

    # generate matplotlib bar chart 
    plotdata = outcome[:3000]  # only plot first 3000 runs
    plt.figure('Outcome by Case (showing first {} runs)'.format(len(plotdata)),
               figsize=(16, 5))  # size is width, height in inches
    index = [i + 1 for i in range(len(plotdata))]
    plt.bar(index, plotdata, color='black')
    plt.xlabel('Simulated Lives', fontsize=18)
    plt.ylabel('$ Remaining', fontsize=18)
    plt.ticklabel_format(style='plain', axis='y')
    ax = plt.gca()
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}"
                                                         .format(int(x))))
    plt.title('Probability of running out of money = {}%'.format(odds),
              fontsize=20, color='red')
    plt.show()

# run program
if __name__ == '__main__':
    main()
