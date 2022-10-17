def multiply(*numbers):
 total = 1
 for num in numbers:
  print("num: " + str(num))
  total *= num
 return total 


result = multiply(2,3,4,4,5)
print(result)


# tuples = collection of objects CANNOT MODIFY!
# iterable