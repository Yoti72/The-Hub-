import math

x = int(input('What is your income for the month: '))

print()
print("Please enter below your expenses below.")
food = int(input("Amount spent on food: "))
housing = int(input("Amount spent on housing and utilities: "))
transportation = int(input("Amount spent on transportation: "))
memberships = int(input("Amount spent on your cell phone and any memberships: "))
savings = int(input("Amount you save every month: "))
health = int(input("Amount spent on any type of insurance or health needs: "))
miscellaneous = int(input("Amount spent on any other miscellaneous expenses: "))
total_expense = (food + housing + transportation + memberships + savings + health + miscellaneous)
print()
#50/30/20 = needs/wants/savings
needs = (food + housing + transportation + health)
wants = (memberships + miscellaneous)
savings20 = (savings)
print()
print("Total income:")
per_needs = (needs / x)
print("Necessities:",round(per_needs * 100), "%")
a = abs((round(per_needs * 100) - 50))
per_wants = (wants / x)
print("Wants:",round(per_wants * 100), "%")
b = abs((round(per_wants * 100) - 30))
per_savings = (savings20 / x)
print("Savings:", round(per_savings * 100), "%")
c = abs((round(per_savings * 100) - 20))

g_needs = (x * .5)
h_wants = (x * .3)
j_savings = (x * .2)
print()

leftover_needs = abs(g_needs - needs)
leftover_wants = abs(h_wants - wants)
leftover_savings = abs(j_savings - savings)
print()
print()
print("-------------------------------------------")
if (per_needs > 50):
  print("Your necessities dont make up more than 50% of your total income which is good, you can afford to spend", str(round(a)), "% or", leftover_needs, "dollars more of your monthly income on necessities if you wanted.")
elif (per_needs < 50):
  print("Your necessities make up more than 50% of your total income which is not optimal, you exceed the recommended monthly budget by", str(a), "% or by", leftover_needs, "dollars.")
elif (per_needs == 50):
  print("Your necessities make up 50% of your total income which is highly recommended.")

print()

if (per_wants < 30):
  print("Your unnecessary purchases dont make up more than 30% of your total monthly income which is good, you can afford to spend", str(round(b)), "% or", leftover_wants, "dollars more of your monthly income on unnecessary purchases or save it for a rainy day.")
elif (per_wants > 30):
  print("Your unnecessary purchases make up more than 30% of your total monthly income which is not optimal, you exceed the recommended monthly budget by", str(b), "% or by", leftover_wants,"dollars.")
elif (per_wants == 30):
  print("Your unnecessary purchases make up 30% of your total monthly income which is highly recommended for a normal monthly budget.")

print()

if (per_savings < 20):
  print("Your savings dont make up 20% of your total monthly income which is not recommended, you can should save at least", str(round(c)), "% or", leftover_savings, "dollars more of your monthly income on your savings and any debt.")
elif (per_savings > 20):
  print("Your savings make up more than 20% of your total monthly income which is always good if you can afford it, you exceed the recommended monthly budget by", str(c), "% or",leftover_savings,"dollars, keep up the good work also use this extra savings to pay off any debt or late payments.")
elif (per_saving == 20):
  print("Your savings make up 20% of your total monthly income which is recommended, but you can always save more for a rainy day.")

if (per_savings > 20):
  s = 33.3
elif (per_savings == 20):
  s = 23.3
elif (per_savings < 20):
  s = 13.3

if (per_needs < 20):
  n = 33.3
elif (per_needs == 20):
  n = 23.3
elif (per_needs > 20):
  n = 13.3

if (per_wants > 20):
  w = 33.4
elif (per_wants == 20):
  w = 23.3
elif (per_wants < 20):
  w = 13.3


grading_scale = int(s + n + w)
print("-------------------------------------------")
print()
print()
print("You get a", grading_scale, "percent on your budgeting for this month." )