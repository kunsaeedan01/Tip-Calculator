print("Welcome to the tip calculator")
bill = float(input("What was the total bill: "))
tip_percent = int(input("Choose the percentage of the tip: "))
people = int(input("How many people split the bill: "))

total_tip = (bill * tip_percent)/100
total_bill  = bill + total_tip
bill_per_person = total_bill/people

print(format(bill_per_person, '.2f'))
