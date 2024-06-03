'''Um furto de celular ocorreu na cidade de Recife e você foi contratado para
desenvolver um programa que possa ajudar na identificação de uma das
pessoas envolvidas. Sua tarefa é criar uma solução utilizando vetores que faça
cinco perguntas para uma pessoa, sendo elas:
• "Você conhece a vítima do furto?"
• "Você esteve no local do furto?"
• "Você mora perto da vítima?"
• "A vítima lhe devia?"
• "Você já trabalhou com a vítima?“
Com base nas respostas, se a pessoa responder positivamente a duas
questões, ela será classificada como "Suspeita". Se responder positivamente a
três ou quatro questões, será classificada como "Cúmplice". Se responder
positivamente a todas as cinco perguntas, será classificada como "Ladrão".
Caso contrário, será classificada como "Inocente".'''

resposta = []
cont = 0

print("Responda com sim ou não para as respostas abaixo.")
resposta.append(input("Você conhece a vítima do furto?"))
resposta.append(input("Você esteve no local do furto?"))
resposta.append(input("Você mora perto da vítima?"))
resposta.append(input("A vítima lhe devia?"))
resposta.append(input("Você já trabalhou com a vítima?"))

for i in resposta:
    if i == 'sim':
        cont += 1
    elif i == 'não':
        cont += 0

if cont == 2:
    print("Essa pessoa é Suspeita")
elif cont == 3 or cont == 4:
    print("Essa pessoa é Cúmplice")
elif cont == 5:
    print("Ladrão")
else: 
    print("Essa pessoa é Inocente")        