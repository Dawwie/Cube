import random
i = 0
while True:
  i = i + 1
  cube1 = random.randint(1,6)
  cube2 = random.randint(1,6)
  suma = cube1+cube2
  print(input(),str(i)+".","Wylosowane liczby to:",cube1,"i",cube2,"\n","Przesuń się o ",end="")
  if 1 < suma < 5:
    print(suma,"oczka.")
  elif suma == 1:
    print(suma,"oczko.")
  else:
    print(suma,"oczek.")
  if cube1 != cube2:
    print("*************************************")