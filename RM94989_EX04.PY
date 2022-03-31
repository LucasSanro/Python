# imports

import time
# head

print("####__Gerador de senhas__####")

# solicitação de dados

minutos = int(input(
    "Por favor digite os minutos do exato momento que está tentando gerar as senha!: "))
fator = minutos
c = 1
print("Calculando {}!......".format(minutos))
time.sleep(3)

# calculo

while fator > 0:
    print("{}".format(fator), end="")
    print(" x " if fator > 1 else " = ", end="")
    c *= fator
    fator -= 1
print("{}".format(c))
print("A SENHA É: LIBERDADE{}".format(c))

# FINISH

time.sleep(3)
print("FIM DA EXECUÇÂO")
exit()
