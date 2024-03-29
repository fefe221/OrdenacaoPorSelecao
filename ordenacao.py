import random

class Ordenacao():
    def buscar_menor(arr):
        menor = arr[0]
        menor_indice = 0
        for i in range(1, len(arr)):
            if arr[i] < menor:
                menor = arr[i]
                menor_indice = i
        return menor_indice
    def ordenacao_por_selecao(arr):
        novo_arr = []
        for i in range(len(arr)):
            menor = Ordenacao.buscar_menor(arr)
            novo_arr.append(arr.pop(menor))
        return novo_arr


# Definindo o tamanho da lista e o intervalo dos números aleatórios
tamanho_lista = 100
min_valor = 1
max_valor = 1000

minha_arr = [random.randint(min_valor, max_valor) for _ in range(tamanho_lista)]

print(Ordenacao.ordenacao_por_selecao(minha_arr))