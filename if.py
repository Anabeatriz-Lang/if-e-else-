def classificar_idade():
    idade = int(input("Digite sua idade:"))

if idade < 13:
    print("Voce é uma Criança.")
elif idade >= 13 and idade < 18:
    print("Voce é um Adolescente.")
elif idade >= 18 and idade < 60:
    print("Voce é um Adulto.")
else:
    print("Voce é um Idoso.")


classificar_idade()