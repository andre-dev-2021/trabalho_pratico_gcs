
from arvore import ArvoreBinaria


def main():
    arvore = ArvoreBinaria()

    # Monta uma árvore de exemplo com valores em diferentes posições.
    valores = [10, 5, 15, 3, 7, 12, 20]

    for valor in valores:
        arvore.inserir(valor)

    # A travessia em ordem apresenta os valores do menor para o maior.
    print("=== ARVORE BINARIA DE BUSCA ===")
    print("Valores inseridos:", valores)
    print("Valores em ordem crescente:", arvore.em_ordem())

    # Compara a busca de um valor presente com outro que não foi inserido.
    print("O valor 7 existe?", arvore.buscar(7))
    print("O valor 99 existe?", arvore.buscar(99))


if __name__ == "__main__":
    main()
