frase = str(input('Digite uma frase qualquer: ')).upper().strip()
print("A letra 'A' aparece {} vezes, na frase".format(frase.count('A')))
print("A 1° letra 'A' apareceu na posição {}°".format(frase.find('A')+1))
print("A última letra 'A' apareceu na posição {}°".format(frase.rfind('A')+1))