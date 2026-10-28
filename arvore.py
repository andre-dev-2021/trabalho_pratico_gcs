
class No:
    def __init__(self, valor):
        """Cria um nó com um valor e sem filhos."""
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        """Inicializa uma árvore vazia."""
        self.raiz = None

    def inserir(self, valor):
        """Insere um valor; valores repetidos são ignorados."""
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir(self.raiz, valor)

    def _inserir(self, no, valor):
        """Procura a posição correta do valor a partir do nó informado."""
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir(no.esquerda, valor)

        elif valor > no.valor:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir(no.direita, valor)

    def buscar(self, valor):
        """Retorna True se o valor estiver na árvore; caso contrário, False."""
        atual = self.raiz

        while atual is not None:
            if atual.valor == valor:
                return True
            elif valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        return False

    def em_ordem(self, no):
        if no is None:
            return []
        
        return (
            self.em_ordem(no.esquerda)
            + [no.valor]
            + self.em_ordem(no.direita)
        )

    def minimo(self):
        """Retorna o menor valor armazenado na árvore."""
        if self.raiz is None:
            return None
        atual = self.raiz
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.valor