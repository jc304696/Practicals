header = "Electricity bill estimator\n"
print(header)

AnswerQ1 = float(input("Enter cents per kWh: "))
AnswerQ2 = float(input("Enter use in kWh: "))
AnswerQ3 = float(input("Enter number of billing days: "))

TotalCost = ((AnswerQ1 * 0.01) * AnswerQ2) * AnswerQ3
print("\n")
print("Estimated bill: ${:.2f}".format(TotalCost))


