class No:
    def __init__(self, valor, frequencia, esquerda=None, direita=None):
        self.valor = valor
        self.frequencia = frequencia
        self.esq = esquerda
        self.dir = direita


class Arvore:
    def __init__(self, raiz=None):
        self.raiz = raiz


def frequencia_ordenada(texto) -> list:
    frequencia_completa = []

    for s in 'abcdefghijklmnopqrstuvwxyz ':  # apenas minúsculas e espaço
        freq = texto.count(s)  # a função count conta os caracteres no texto

        if freq > 0:
            no = No(s, freq)  # cria um nó com o valor e a frequência
            frequencia_completa.append(no)  # adiciona o nó à lista

    lista_frequencia_ordenada = sorted(
        frequencia_completa, key=lambda x: x.frequencia)  # ordena a lista
    return lista_frequencia_ordenada


def montar_arvore(lista: list):
    while len(lista) > 1:  # enquanto a lista tiver tamanho suficiente para retirarmos 2 elementos
        a = lista.pop(0)
        b = lista.pop(0)  # retira dois elementos

        # soma os elementos e adiciona aqueles que retiramos à esquerda e direita
        soma = No(a.frequencia + b.frequencia, a.frequencia +
                  b.frequencia, esquerda=a, direita=b)

        lista.append(soma)  # adiciona a soma na lista
        # reordena já com o nó de soma
        lista = sorted(lista, key=lambda x: x.frequencia)
    return lista


def gerar_dicionario(dicionario, raiz, caminho_binario):
    if raiz is not None:
        if raiz.esq is None and raiz.dir is None:  # se é uma folha
            dicionario[raiz.valor] = caminho_binario  # adiciona 0 ou 1
        # se não, procura pelo resto da árvore, e adiciona 0 quando for para esquerda, e 1 para direita
        gerar_dicionario(dicionario, raiz.esq, caminho_binario + "0")
        gerar_dicionario(dicionario, raiz.dir, caminho_binario + "1")


def imprimir_dicionario(dicionario):
    print("\n-> Dicionário:")
    # sorted usado para mostrar o resultado em ordem alfabetica
    for key, value in sorted(dicionario.items()):
        print(f"{key}: {value}")  # mostra a letra e depois o código


def codificar(dicionario, string):
    codigo = list()
    for i in range(len(string)):
        # achamos o caractere do texto correspondente no nosso próprio dicionario e adicionamos à lista
        codigo.append(dicionario[string[i]])

    return ''.join(codigo)  # para mostrar tudo junto, sem aspas


def imprimir_frequencia(lista_frequencia):
    print("\n-> Frequência dos caracteres:")
    # sorted usado para mostrar o resultado em ordem alfabética, por isso key é x.valor, analisamos o caractere
    for no in sorted(lista_frequencia, key=lambda x: x.valor):
        print(f"{no.valor}: {no.frequencia}")


# texto de entrada, transformamos para lower case
texto = input("Digite: ").lower()

# ordenamos o texto com as frequências
lista_frequencia = frequencia_ordenada(texto)
imprimir_frequencia(lista_frequencia)  # imprimimos a frequência dos caracteres

lista_arvore = montar_arvore(lista_frequencia)  # montamos a árvore

# definimos a raíz como o primeiro e único elemento da lista (árvore já está montada)
raiz = lista_arvore[0]
arvore = Arvore(raiz)

dicionario = {}  # usaremos um dicionário para organizar os caracteres e os códigos
gerar_dicionario(dicionario, arvore.raiz, "")
imprimir_dicionario(dicionario)

codifica = codificar(dicionario, texto)  # codifica o texto original
print(f'\n-> Texto codificado: ', codifica)
