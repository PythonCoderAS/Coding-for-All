# Mr Burns
# Coding for All
# Student: Aoyan Sarkar


### Input ###

SalesPersonName = input("What is your name?: ")
SalesAmount = float(input("How much did you sell?: "))
CommissionRate = float(input("What is your comission rate (in percent)?:"))

### Calculations ###
CommissionEarned=(SalesAmount*CommissionRate)/100

### Output ###

print(SalesPersonName+", your sales are: $"+str(SalesAmount)+" and your commission is: $"+str(CommissionEarned))
