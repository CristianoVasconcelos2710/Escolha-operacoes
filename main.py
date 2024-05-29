n1 = float(input("Escolha um número:\n"))
n2 = float(input("Escolha outro número:\n"))
print("Digite o número 1 para somar")
print("Digite o número 2 para subtrair")
print("Digite o número 3 para multiplicar")
print("Digite o número 4 para dividir")
op = input("Digite a operação:\n")

if op =='1':
  soma = n1+n2
  print(f"O resultado é:\n{soma}")

elif op =='2':
  sub = n1-n2
  print(f"O resultado é:\n{sub}")

elif op =='3':
  mult = n1*n2
  print(f"O resultado é:\n{mult}")

else:
  div = n1/n2
  print(f"O resultado é:\n{div:,.2f}")
