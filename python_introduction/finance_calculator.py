# User input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calcul of mensuel saving
monthly_savings = monthly_income - monthly_expenses

# Projected saving of 5%
projected_savings = monthly_savings * 12 * 1.05  

# print resultat
print(f"Your monthly savings are ${monthly_savings:.0f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")