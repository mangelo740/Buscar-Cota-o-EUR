
# ESSA NOTA A ELA TEM UMA APROVAÇÃO = PESO DE 3,5
notaA = float(input("Digita a nota A: "))
notaB = float(input("Digita a nota B: "))

notaAB = (notaA + notaB)/2
notaaeb = notaA + notaB

if notaAB >= 7.5:
    print(f"APROVADO!!! Sua média foi de {notaAB} Sua notaA + notaB foi de {notaaeb}")
else:
    print(f"REPROVADO!!! Sua média foi de {notaAB}")
