num = 5
for i in range (1, num + 1):
      sp = (num - i) * "  "
      print(sp, end = " ")
      for k in range(i, 1, -1):
          print("*", end = " ")
      for j in range(1, i + 1):
          print("*", end = " ")
      print()
