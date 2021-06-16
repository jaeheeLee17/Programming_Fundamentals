# Loan repayment calculation service
# This is the program calculating the loan repayment amount for clients.
#
# Input parameters:
# principal(p) : Only integers equal or greater than one million are allowed
# years(y) : Only integers equal or greater than one are allowed
# annual interest rate(r) : Only floating point numbers from 0.0 to 100.0 are allowed
# Output parameters:
# annual repayment amount(d), monthly repayment amount(d / 12), total repayment amount(d * y)
#
# Developers : Hacktree
# Development date : 2021/06/16 (Version 1.0)

# Input and check input value
print("Welcome to loan repayment calculation service")
p = int(input("How much is the principal? (We only count over one million won.) "))
y = int(input("How many years is the repayment period? "))
r = float(input("What percent is the interest rate? "))
# Calcualte repayment amount
d = ((1 + (r / 100)) ** y * p * (r / 100)) // ((1 + (r / 100)) ** y - 1)
d = int(d)
# Print Output
print("We will inform you about the loan repayment details.")
print("If you repay once a year, you have to pay {} won for each year.".format(d))
print("If you repay once a month, you have to pay {} won for each month.".format(d // 12))
print("The total repayment amount until the repayment is completed is {} won.".format(d * y))
print("Thank you for using our service.")
print("I hope you to see again.")
