#escreva um programa que solicite um determinado numero de dias em seguida exiba o quanto esses dias valem em horas minutos e segundos 
qtnddias = int(input("Digite um número de dias : "))
qntdhoras = qtnddias * 24 
qntdminutos = qtnddias * 1440
qntdsegundos = qtnddias * 86400
print("Esse dia tem este numero de horas : ", qntdhoras )
print("Esse dia tem este numero de minutos : ", qntdminutos)
print("Esse dia tem este numero de segundos : ", qntdsegundos)
