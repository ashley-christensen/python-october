weight = input("Weight: ")
type_input = input("(K)gs or (L)bs: ")

if type_input.lower() == 'l':
 lbs = str(float(weight) * 0.45359237)
 print("Weight in kg: " + lbs)
if type_input.lower() == 'k':
  kilos = str(float(weight) * 2.2)
  print("Weight in lbs: " + kilos)