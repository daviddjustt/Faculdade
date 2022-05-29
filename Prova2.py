#Entrada#
questões = int(input("O número de questões que a prova terá"))
gabarito = str(input("O gabarito que a prova terá"))
respostas = str(input("Opções escolhidas pelo candidato"))
#transformando as palavras em váriáveis e em listas
a = questões

b = gabarito
x = len(b)

c = respostas
y = len(c)

#Deixando o número de QUESTÕES, RESPOSTAS e GABARITO iguais#
if a != x:
    print(" O número de questões não condiz com o gabarito")
    exit()
elif y != a:
    print(" O número de gabarito não condiz com resposta")
    exit()
elif x != y:
    print(" O número de resposta não condiz com questões")
    exit()
else:
    pass

#Limitando os caracteres de QUESTÕES#
a = questões
if a >= 80:
    print("O valor máximo de questões é 80")
    exit()
elif a <= 1:
    print("O valor mínimo de questões é 1")
    exit()
#Limitando os caracteres de GABARITO#

if (x) >= 80:
    print("O valor máximo de respostas é 80")
    exit()
elif (x) <= 1:
    print("O valor mínimo de respostas é 1")
    exit()
#Limitando os caracteres de RESPOSTAS#

if (y) >= 80:
    print("O valor máximo de respostas no gabarito é é 80")
    exit()
elif (y) <= 1:
    print("O valor mínimo de respostas no gabarito é é 1")
    exit()
#Os caracteres válidos para as respostas e o gabarito#
l1 = gabarito
l2 = respostas
l3 = ["A", "B", "C", "D", "E"]

if(set(l3) == set(l2)):
   pass
elif(set(l3) == set(l1)):
    pass
else:
    print("Valores diferentes de A,B,C,D,E não serão considerados")
#comparando as respostas#
escolhas = list(respostas)
gabaritos = list(gabarito)

acertos = 0

for escolhas, gabaritos in zip(escolhas, gabaritos):
    acertos += (escolhas == gabaritos)
print("O aluno(a) acertou{}".format(acertos))

