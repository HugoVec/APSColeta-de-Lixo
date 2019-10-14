
while True:
  try:
      number = float(input('Insira a Latitude'))
      number2 = float(input('Insira a Latitude2: '))
  except ValueError:
     print("Not an integer!")
     continue
  else:
     print("Yes an integer!")
     break

