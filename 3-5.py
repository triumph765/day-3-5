
print("Welcome to ")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



# Kanye West
# Kim Kardashian

m = name1.lower()
print(m)
f = name2.lower()
print(f)

t = m.count('t')
print(f'T occurs {t} times')
r = m.count('r')
print(f'R occurs {r} times')
u = m.count('u')
print(f'U occurs {u} times')
e = m.count('e')
print(f'E occurs {e} times')
sum = int(t + r + u + e)
print(f'total = {sum}')

l = f.count('l')
print(f'L occurs {l} times')
o = f.count('o')
print(f'O occurs {o} times')
v = f.count('v')
print(f'V occurs {v} times')
e = f.count('e')
print(f'E occurs {e} times')
sum1 = int(l + o + v + e)
print(f'total = {sum1}')

s = str(sum) + str(sum1)
print(f'Your score is {s}')

scores = int(s)
if scores >= 90 or scores <= 10:
  print(f"Your score is {scores}, you go together like coke and mentos.")
elif 40 <= scores <=50:
  print(f"Your score is {scores}, you are alright together.")
else:
  print(f"Your score is {scores}.")