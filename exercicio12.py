#escreva um programa que pergunte o valor total da conta e em seguida pergunte quantos clientes existem, divida conta pelos clientes e exiba o quanto cada cliente deve pagar
#seguida da mensagem cada cliente deve pagar: ...... 

valortotal = int(input("Qual valor total do conta ? "))
qtndclientes = int(input("Quantos clientes existem ? "))
operacao = valortotal / qtndclientes
print("Cada cliente deve pagar : ", operacao)