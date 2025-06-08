a = int(input('Enter a number: '))

if a < 0:
  print('Number is -ve')
  
else:
  def factorial(a):
    if a <2:
      return 1
    else:
     return a*factorial(a-1)
  ans = factorial(a)
  print('Factorial of', a, 'is:', ans)
