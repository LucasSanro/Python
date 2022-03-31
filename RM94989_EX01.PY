# imports
import time

# Head

print("Bem vindo ao sistema de calculo de comissão da FIAP ON")
print("Temos os seguintes niveis de Assinatura: Basic, Silver, Gold e Platinum ")

# solicitação de dados

nivel = str(input("Por favor informe seu nivel de assinatura: ")).upper()
comissao = float(input("Por favor informe qual foi seu faturamento atual: "))

# Calculo

if nivel == "BASIC":
    valorComissão = comissao*0.3
    print("o valor da comissão é de {}".format(valorComissão))
elif nivel == "SILVER":
    valorComissão = comissao*0.2
    print("o valor da comissão é de {}".format(valorComissão))
elif nivel == "GOLD":
    valorComissão = comissao*0.1
    print("o valor da comissão é de {}".format(valorComissão))
elif nivel == "PLATINUM":
    valorComissão = comissao*0.05
    print("o valor da comissão é de {}".format(valorComissão))
else:
    print("Por favor informe o nivel de assinatura!")

# Finalização

time.sleep(3)
print("FIM DA EXECUÇÂO")
exit()
