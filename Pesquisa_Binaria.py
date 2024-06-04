def pesquisa_binaria(lista, item):
    baixo = 0 
    alto = len(lista) - 1 
    while baixo <= alto: 
        meio = round((baixo + alto) / 2 )
        chute = lista[meio]
        if chute == item: 
            return meio
        if chute > item: 
            alto = meio - 1
        else: 
            baixo = meio + 1
    return None 

minha_lista = []
qnt = int(input("Digite a quantidade de numeros que a lista vai ter: \n"))

for i in range(qnt):
    minha_lista.append(int(input("Digite um numero: ")))

numero = int(input("Digite um número inteiro para palpite, que não tenha virgula nem seja negativo: \n"))
minha_lista.sort()
print("O numero desejado esta na posição :",pesquisa_binaria(minha_lista, numero)) # => 1 
