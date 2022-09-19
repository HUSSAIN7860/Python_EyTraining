# An integer is a palindrome when it reads the same backward as forward.
n = input('enter the number here :')
if n == n[::-1]:
  print('Numbers is Palindrome')
else:
  print('Not a Palindrome Number')
