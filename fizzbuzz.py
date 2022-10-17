def fizz_buzz(input):
 while 0 <= input:
  if input % 3 == 0 and input % 5 == 0:
   print("fizzbuzz")
  elif input % 3 == 0:
   print("fizz")
  elif input % 5 == 0:
   print("buzz")
  else:
   print(input) 
  input = input - 1

fizz_buzz(16) 