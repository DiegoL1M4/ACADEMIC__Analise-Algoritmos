
class BinarySearch:
    def busca_binaria(lista, inicio, fim, elemento):
        meio = ((fim - inicio) // 2) + inicio

        if lista[meio] == elemento or inicio >= fim:
            return meio
        elif lista[meio] < elemento:
            return BinarySearch.busca_binaria(lista, meio+1, fim, elemento)
        else:
            return BinarySearch.busca_binaria(lista, inicio, meio-1, elemento)


    def insertionsort_busca_binaria(lista):
        for i in range(len(lista)):
            elemento = lista[i]
            j = i-1

            posicao = BinarySearch.busca_binaria(lista, 0, j, elemento)

            while j >= posicao:
                lista[j+1] = lista[j]
                j = j-1

            if lista[posicao] <= elemento:
                lista[posicao+1] = elemento
            else:
                lista[posicao+1] = lista[posicao]
                lista[posicao] = elemento
                