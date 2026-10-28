
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir(self.raiz, valor)

    def _inserir(self, no, valor):
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
        atual = self.raiz

        while atual is not None:
            if atual.valor == valor:
                return True
            elif valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        return False

    def em_ordem(self, no=None):
        if no is None:
            no = self.raiz
            if no is None:
                return []
    
    def minimo(self):
        """Retorna o menor valor armazenado na árvore."""
        if self.raiz is None:
            return None
        atual = self.raiz
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.valor

        
        return (
            self.em_ordem(no.esquerda)
            + [no.valor]
            + self.em_ordem(no.direita)
        )
