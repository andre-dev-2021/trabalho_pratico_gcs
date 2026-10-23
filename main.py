
from arvore import ArvoreBinaria


def main():
    arvore = ArvoreBinaria()

    # Inserindo valores na arvore
    valores = [10, 5, 15, 3, 7, 12, 20]

    for valor in valores:
        arvore.inserir(valor)

    # Exibindo os valores
    print("=== ARVORE BINARIA DE BUSCA ===")
    print("Valores inseridos:", valores)
    print("Valores em ordem crescente:", arvore.em_ordem())

    # Testando a busca
    print("O valor 7 existe?", arvore.buscar(7))
    print("O valor 99 existe?", arvore.buscar(99))


if __name__ == "__main__":
    main()
