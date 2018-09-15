bill_amount = input("Enter the bill amount")
bill_amount = float(bill_amount)
tip = bill_amount *.15
tip = float(tip)
total_amount = bill_amount + tip
print("Total Amount to be paid is %s", total_amount)