# imports
import time
# Head

print("Resultado da votação dos alunos")
print("Digite o resultado da votação seguindo a ordem abaixo")
print("Segunda-feira, Terça-feira, Quarta-feira, Quinta-feira e Sexta-feira")

# solicitação de dados

segunda = int(input("Digite o número de votos para Segunda feira: "))
terca = int(input("Digite o número de votos para Terça feira: "))
quarta = int(input("Digite o número de votos para Quarta feira: "))
quinta = int(input("Digite o número de votos para Quinta feira: "))
sexta = int(input("Digite o número de votos para Sexta feira: "))

# resultado

print("Resultado da votação:")
print(" Segunda feira: {}".format(segunda))
print(" Terça-feira: {}".format(terca))
print(" Quarta-feira: {}".format(quarta))
print(" Quinta-feira: {}".format(quinta))
print(" Sexta-feira: {}".format(sexta))

# Calculo

if (segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta):
    print("Segunda é o dia selecionado para as lives!")

elif(terca > segunda and terca > quarta and terca > quinta and terca > sexta):
    print("Terça é o dia selecionado para as lives!")

elif(quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta):
    print("Quarta é o dia selecionado para as lives!")

elif(quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta):
    print("Quinta é o dia selecionado para as lives!")

elif(sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta):
    print("Sexta é o dia selecionado para as lives!")
else:
    print("Favor rever a votação!")

time.sleep(3)
print("FIM DA EXECUÇÂO")
exit()
