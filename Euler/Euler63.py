

def return_digits(n):
   return len(str(n))

for i in range(1, 100):
   k = 0
   j = 1
   power = 0
   while return_digits(power) <= i:
      power = j**i
      if return_digits(power) == i:
         k+=1
         print(power)
      j = j+1
   solutions[i] = k


vals = [v for k, v in solutions.items()]