# Menssagen(em qual numero vc pensou)
#Entrada: 45
#Saída: Esse é um número ímpar! Gostaria de verificar outro

parar = input("Quer continuar? [S/N] ")

while parar == "s":
    num = int(input("Em qual número você pensou?"))
    if num % 2 == 0:
      print("Esse é um número par!")
    else:
      print("É um número impar!")
      parar = input("Quer continuar? [S/N] ")

#GabrielVieira