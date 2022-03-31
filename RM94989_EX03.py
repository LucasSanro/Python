
# imports

import time

# Head

print("Notas dos alunos")
print("Digite as notas dos alunos: ")

# variaveis
numAlunopar = "0"
numAlunoimp = "0"
notapar = 0, 0
notaimp = 0, 0
notaTotalimp = 0
notaTotalpar = 0

# loop
loop = 25

# Solicitação de dados/calculos

for x in range(0, loop):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES")
    valid = False
    while valid == False:
        numAlunoimp = int(input("Por favor informe o Rm do aluno: "))
        if(numAlunoimp % 2):
            valid = True
        else:
            print("Verificar o numero do aluno")

    notaimp = float(input("Por favor informe a nota do aluno: "))
    notaTotalimp = notaimp+notaTotalimp

for x in range(0, loop):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    valid = False
    while valid == False:
        numAlunopar = int(input("Por favor informe o Rm do aluno: "))
        if(numAlunopar % 2 == False):
            valid = True
        else:
            print("Verificar o numero do aluno")
    notapar = float(input("Por favor informe a nota do aluno: "))
    notaTotalpar = notapar+notaTotalpar

# Resultado

print("#####- MEDIA DOS ALUNOS - #####")
mediaimp = notaTotalimp/loop
mediapar = notaTotalpar/loop
print("a média de notas do lado PAR é {}".format(mediapar))
print("a média de notas do lado IMPAR é {}".format(mediaimp))
if mediaimp > mediapar:
    print("O lado IMPAR tem a média superior ao lado PAR!")
else:
    print("O lado PAR tem a média superior ao lado IMPAR! ")

# FINISH
time.sleep(3)
print("FIM DA EXECUÇÂO")
exit()
