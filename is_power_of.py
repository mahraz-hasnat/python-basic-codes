#is_power_of function return whether the number is a power of the given base
def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == base**0

  # Recursive case: keep dividing number by base.
  return is_power_of( number-base+1, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False
