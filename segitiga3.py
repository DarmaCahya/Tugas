a = int(input())

for i in range(a):
  for j in range(a+1):
    print(" ", end="")
  for k in range(i+1):
    print("*", end="")
  a = a-1
  print()