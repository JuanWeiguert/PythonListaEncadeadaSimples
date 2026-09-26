class Nodo:

    def __init__(self, numero, cor, proximo=None):
        self.numero = numero
        self.cor = cor
        self.proximo = proximo

class ListaEncadeadaSimples:

    def __init__(self):
        self.head = None
        self.V = 1
        self.A = 201

    def inserirSemPrioridade(self, nodo):
        if self.head == None:
            self.head = nodo

        else:
            nodo_atual = self.head

            while nodo_atual.proximo != None:
                nodo_atual = nodo_atual.proximo

            nodo_atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if self.head == None:
            self.head = nodo

        elif self.head.cor == "V":
            nodo.proximo = self.head
            self.head = nodo

        else:
            nodo_atual = self.head

            while nodo_atual.proximo != None and nodo_atual.proximo.cor == "A":
                nodo_atual = nodo_atual.proximo

            nodo.proximo = nodo_atual.proximo
            nodo_atual.proximo = nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A ou V): ")

        if cor == "V":
            numero = self.V
            self.V += 1

            novo_nodo = Nodo(numero, cor)

            if self.head == None:
                self.head = novo_nodo

            else:
                self.inserirSemPrioridade(novo_nodo)

        elif cor == "A":
            numero = self.A
            self.A += 1
            novo_nodo = Nodo(numero, cor)

            if self.head == None:
                self.head = novo_nodo

            else:
                self.inserirComPrioridade(novo_nodo)

        else:
            print("Cor inválida. Digite 'A' ou 'V'.")

    def imprimirListaEspera(self):
        fila = "Lista de espera: "

        nodo = self.head

        while nodo != None:
            fila += f"[{nodo.cor} - {nodo.numero}]"

            if nodo.proximo != None:
                fila += " -> "

            nodo = nodo.proximo

        print(fila)

    def atenderPaciente(self):
        nodo = self.head

        if nodo != None:
            print(f"Atendendo paciente com o cartão {nodo.cor} e número {nodo.numero}")
            self.head = nodo.proximo

        else:
            print("Não há pacientes na lista de espera.")


lista = ListaEncadeadaSimples()

while True:
    print('1 - Adicionar paciente na lista')
    print('2 - Mostrar pacientes na lista de espera')
    print('3 - Atender paciente')
    print('4 - Sair')

    op = int(input("Escolha uma opção: "))
    if op == 1:
        lista.inserir()

    elif op == 2:
        lista.imprimirListaEspera()

    elif op == 3:
        lista.atenderPaciente()

    elif op == 4:
        print("Saindo...")
        break

    else:
        print("Opção inexistente. Tente novamente.")

