i = 2

while(i==2):
  v1 = int(input("Digite um valor: "))
  v2 = int(input("Digite outro: "))  

  if(v1 > 0 and v2 > 0):
    print("Primeiro")
  elif(v1 > 0 and v2 <0):
    print("Quarto") 
  elif(v1 < 0 and v2 < 0):
    print("Terceiro")
  elif(v1 < 0 and v2 > 0):
    print("Segundo")
  else:
    i+=1
   

