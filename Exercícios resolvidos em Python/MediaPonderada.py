# Calcula a média das três notas e mostra se o aluno foi aprovado, reprovado ou está na recuperação

notaum = float(input("Digite a primeira nota: "))
notadois = float(input("Digite a segunda nota: "))
notatres = float(input("Digite a terceira nota: "))

media = (notaum*2 + notadois*3 + notatres*5)/10
print("A média do aluno é : ", media)

if(media>0 and media<5):
    print("Aluno reprovado")
elif(media>=5 and media < 7):
    print("Aluno na recuperação")
else:
    print("Aluno aprovado")

