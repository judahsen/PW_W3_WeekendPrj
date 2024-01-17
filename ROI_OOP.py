# Bigger Pockets automated rental propety calculator to calculate rental property return on investment.

print("""How To Use the Rental Property Calculator                                 
\nUsing the BiggerPockets Rental Property Calculator is a straightforward process that allows you to analyze any rental property deal with precision. To make the most of this tool, you'll need specific information about the property and your financial situation.
\nLoan Details: Specify your down payment percentage, interest rate, loan term (e.g., 30 years), and whether you're paying points on the loan. These details determine your financing terms. An investor-friendly lender can help you get the best funding for your strategy.
\nIncome: Enter the estimated monthly rental income. You can gather this information from rental listing sites, local market knowledge, or BiggerPockets Insights (if you have access).
\nExpenses: Include all relevant expenses, such as property taxes, insurance, utilities (if you're responsible), repairs and maintenance, capital expenditures, property management fees (if applicable), HOA fees (if applicable), garbage, sewer, and vacancy rate.
\nAnalysis: Once you've input all the necessary data, the calculator generates a comprehensive report. You'll find details about your annualized return, cash flow, cash-on-cash return, cap rate, and more. These metrics help you assess the profitability of the deal.
\nFine-Tuning: Feel free to adjust your assumptions and see how they impact the results. For instance, you can experiment with different rent values, vacancy rates, or financing options to evaluate various scenarios
""")
class ROI_calculator():
    
    def __init__(self, total_monthly_income=0, total_monthly_expenses=0, total_investment=0):
        self.total_monthly_income = total_monthly_income
        self.total_monthly_expenses = total_monthly_expenses
        self.total_investment = total_investment
    
    def total_income(self):
        rental_income = float(input("Enter the rent amount:"))
        laundry_cost = float(input("Enter the charge to do Laundry:"))
        storage_fee = float(input("Enter the Storage fee:"))
        misc_costs = float(input("Enter other Misc fees:"))
        self.total_monthly_income = rental_income + laundry_cost + storage_fee + misc_costs
        return self.total_monthly_income

    def expenses(self):
        tax_amount = float(input("Enter the amount for Tax Amount:"))
        insurance = float(input("Enter the Insurance Amount:"))
        utility = float(input("Enter the Utility Amount:"))
        hoa = float(input("Enter the HOA fee :"))
        vacancy = float(input("Enter Vacancy Reserve Amount:"))
        repairs = float(input("Enter repair costs:"))
        cap_ex = float(input("Enter CapEx costs:"))
        property_management = float(input("Enter property Manager Salary:"))
        mortgage = float(input("Enter Monthly Mortgage amount:"))
        self.total_monthly_expenses = tax_amount + insurance + utility + hoa + vacancy + repairs + cap_ex + property_management + mortgage
        return self.total_monthly_expenses
    
    def investment_info(self):
        down_payment = float(input("Enter The Down Payment:"))
        closing_costs = float(input("Enter your Closing costs:"))
        rehab_budget = float(input("Enter your Rehab Budget:"))
        misc_invest = float(input("Enter other small investments:"))
        self.total_investment = down_payment + closing_costs + rehab_budget + misc_invest
        return self.total_investment
    
    def roi_generator(self):
        monthly_cash_flow = self.total_monthly_income - self.total_monthly_expenses
        annual_cash_flow = monthly_cash_flow * 12
        roi = annual_cash_flow / self.total_investment * 100
        print(f"Return on Investment (ROI): {roi}%")
    
    def runner(self):
        while True:
            user_input = input("Select an Option: Enter Income/Enter Expenses/Enter Investment/Run Analysis/Quit: ")
            if user_input == "Enter Income":
                self.total_monthly_income = self.total_income()
            elif user_input == "Enter Expenses":
                self.total_monthly_expenses = self.expenses()
            elif user_input == "Enter Investment":
                self.total_investment = self.investment_info()
            elif user_input == "Run Analysis":
                self.roi_generator()
            elif user_input == "Quit":
                break
            else:
                print("Invalid Entry")

customer = ROI_calculator()
customer.runner()
