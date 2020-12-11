# Make a function that prints the sum of every element in an array that is greater than 10.

a = [13,11,7,4,63,9,24,5]
count = 0

for num in a:
  if num>10:
    count+=num

print(count)