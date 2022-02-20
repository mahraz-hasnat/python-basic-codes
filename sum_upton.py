#the sum_positive_numbers function  is recursive function that returns the sum of all positive numbers between the number n received and 1.
def sum_positive_numbers(n):
  if n < 2:
    return 1 
  return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
