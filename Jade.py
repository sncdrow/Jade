print("Olá, meu nome é Jade sua calculadora financeira !!")
tp=input("Deseja calcular juros simples ou juros compostos ?\n")
if(tp=="simples"):
    c=int(input("Digite o valor do capital aplicado:\n"))
    i=float(input("Agora digite o valor da taxa:\n"))
    t=int(input("Escreva por quantos meses o capital foi aplicado:\n"))
    j=c*i/100*t
    print("O juro cobrado é de: {}".format(j))
if(tp=="composto"):
    c=int(input("Digite o valor do capital aplicado:\n"))
    i=float(input("Agora digite o valor da taxa:\n"))
    t=int(input("Escreva por quantos meses o capital foi aplicado:\n"))
    j=c*(1+i/100)**t
    print("O juro cobrado é de: {}".format(j))