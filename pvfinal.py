import os

#JOSÉ RIBAMAR G. DE SOUSA, 20201p2ads0153
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Lista:
    def __init__(self):
        self.topo = None
        self.ultimo = None
        self._size = 0

    # Inserir elementos no final da lista.
    def append(self, elemento):
        # Caso exista um elemento já na lista.
        if self.topo:
            # Inserção quando a lista já possui elementos
            ponto = self.topo
            ls = None
            # Pegar a posição da memória onde não exista nada no próximo 
            while(ponto.proximo):
                ls = ponto
                ponto = ponto.proximo
            ponto.proximo = No(elemento)
            ponto.proximo.ls = ponto
            ponto.ls = ls
            if self.ultimo:
                self.ultimo = ponto.proximo

        # Se não insira o primeiro elemento na lista.
        else:
            # Primeira inserção
            self.topo = No(elemento)
            self.ultimo = No(elemento)
        self._size = self._size + 1

    def __len__(self):
        # Retorna o tamanho da lista.
        return self._size

    def _get_node(self, index):
        ponto = self.topo
        for i in range(index):
            if ponto:
                ponto = ponto.proximo
            else:
                raise IndexError("list index out of range")
        return ponto

    def __getitem__(self, index):
        # Recuperar o valor a partir de []
        # a = lista[6]
        ponto = self._get_node(index)
        if ponto:
            return ponto.dado
        raise IndexError("list index out of range")


    def __setitem__(self, index, elemento):
        # lista[5] = 9
        ponto = self._get_node(index)
        if ponto:
            ponto.dado = elemento
        else:
            raise IndexError("list index out of range")

    def index(self, elemento):
        # Retorna o índice do elemento na lista
        ponto = self.topo
        i = 0
        # for diferente de None
        while(ponto):
            if ponto.dado == elemento:
                return i
            ponto = ponto.proximo
            i = i + 1
        raise ValueError(f'{elemento} is not in list')

##############################################################################################################################

##############################################################################################################################

class aresta(object):
    def __init__(self, origem, destino):
        self.origem = origem
        self.destino = destino

class vertice(object):
    def __init__(self, valor):
        self.valor = valor
        #adiciona vertice
        self.listaAdjacencia = Lista()
        self.timestamp = Lista()
        
        self.cor = None
        self.distancia = None
        #adiciona vertice
    def adicionarAdjacencia(self, destino):
        self.listaAdjacencia.append(destino)

class grafo(object):
    def __init__(self):
        self.Larestas = Lista()
        self.Lvertices = Lista()
        self.tempo = 0

    def adicionarAresta(self, aresta):
        destinoIndex = self.buscarVertice(aresta.destino) # origem
        origemIndex = g.buscarVertice(aresta.origem) # destino
#       print(str(origemIndex) + str(self.buscarVertice(vdestino)) + str(self.buscarAresta(aresta)) )
        if ((self.buscarAresta(aresta) is False)): # se nao tiver aresta ela insere
            self.Larestas.append(aresta)
            self.Lvertices[origemIndex].adicionarAdjacencia(self.Lvertices[destinoIndex])
        else: # se ja existe ela n insere
            print("\033[1;36mAresta ja existe ou vertices nao existem")

    def adicionarVertice(self, vertice): ##        
        if not self.buscarVertice(vertice): # se n tiver vertice ela insere
            self.Lvertices.append(vertice)
        else: # se ñ ela retorna uma msg
            print("\033[1;36mO vertice ja existe!")

    def iniciaBuscaProfundidade(self): # ini cia a busca
        for i in range(0, len(self.Lvertices)): # percorre todas as vertices
            self.Lvertices[i].timestamp = []
            self.Lvertices[i].cor = "\033[1;34m"
        self.tempo = 0
        for i in range(0, len(self.Lvertices)):
            if self.Lvertices[i].cor == "\033[1;34m":
                self.buscaProfundidade(self.Lvertices[i])
        self.printaProfundidade() # retorna a busca
        

    def buscaProfundidade(self, vertice):
        self.tempo += 1
        idx = self.buscarVertice(vertice)
        self.Lvertices[idx].timestamp.append(self.tempo)
        self.Lvertices[idx].cor = "\033[1;32m"
        for v in self.Lvertices[idx].listaAdjacencia:
            if v.cor == "\033[1;34m":
                self.buscaProfundidade(v)
        self.Lvertices[idx].cor = "\033[1;31m"
        self.tempo += 1
        self.Lvertices[idx].timestamp.append(self.tempo)

    def printaProfundidade(self):
        for v in self.Lvertices:
            print("\033[1;34m Vertice: {0} \033[1;32m Visita: {1}° \033[1;31m Elimina: {2}°\033[1;33m".format(v.valor, v.timestamp[0], v.timestamp[1]))



    def iniciaLargura(self, verticeini, pai):
        idx = self.buscarVertice(verticeini)
        if idx is not False:
            self.Lvertices[idx].cor = "\033[1;34m"
        for i in range(0, len(self.Lvertices[idx].listaAdjacencia)):
            if self.Lvertices[idx].listaAdjacencia[i].valor != pai.valor:
                self.iniciaLargura(self.Lvertices[idx].listaAdjacencia[i], self.Lvertices[idx])

    def buscaLargura(self, verticeini, verticefim): # vertice inicial e fi
        idxini = self.buscarVertice(verticeini) #inicio
        idxfim = self.buscarVertice(verticefim) #fim
        self.iniciaLargura(verticeini, verticeini)
        d = 0
        self.Lvertices[idxini].cor = "\033[1;32m"
        self.Lvertices[idxini].distancia = d
        cinzas = []
        cinzas.append(self.Lvertices[idxini])
        while len(cinzas) != 0:
                d += 1
                atual = cinzas.pop(0)
                for i in atual.listaAdjacencia:
                    idx = self.buscarVertice(i)
                    if self.Lvertices[idx].cor == "\033[1;34m":
                        self.Lvertices[idx].cor = "\033[1;32m"
                        self.Lvertices[idx].distancia = d
                        if self.Lvertices[idxfim].valor == self.Lvertices[idx].valor:
                            return self.Lvertices[idx].distancia
                        cinzas.append(self.Lvertices[self.buscarVertice(i)])
                idxatual = self.buscarVertice(atual)
                self.Lvertices[idxatual].cor = "\033[1;33m"
        return -1

    def buscarVertice(self, v): ##valor da lista
        try:
           # indice = [print(x.valor) for x in self.Lvertices].index(v.valor)
            for indice, x in enumerate(self.Lvertices):
                if (x.valor == v.valor):
                    return indice
            return False
        except ValueError:
            return False

    def buscarAresta(self, aresta): # bu
        try:
            for idx,x in enumerate(self.Larestas):
                if (x.origem.valor == aresta.origem.valor) and (x.destino.valor == aresta.destino.valor):
                    return idx
            return False
        except ValueError:
            return False
        
def caso_1(g): # adicionar vertice
    entVertices=input().split(",")
    cont=0
    for i in entVertices:
        entVertices[cont]=i
        cont+=1
    for valor in entVertices:
        v = vertice(valor)
        g.adicionarVertice(v)

def caso_2(g): # adicionar aresta

    entArrestas=input().split(";")
    cont=0
    for _ in entArrestas:
        entArrestas[cont]=entArrestas[cont].replace("(","")
        entArrestas[cont]=entArrestas[cont].replace(")","")
        entArrestas[cont]=entArrestas[cont].split(",")
        cont+=1
    cont=0
    for valor in entArrestas:
        if len(valor) == 2:
            vorigem = vertice(valor[0])
            vdestino = vertice(valor[1])
            origemIndex = g.buscarVertice(vorigem)
            destinoIndex = g.buscarVertice(vdestino)
            if ((destinoIndex is not False) and (origemIndex is not False) ):
                print(f"\033[1;36minseriu: {valor[0]}->{valor[1]}")
                a = aresta(g.Lvertices[origemIndex], g.Lvertices[destinoIndex])
                g.adicionarAresta(a)

def caso_3(g): #Imprime grafo    
    print("\033[1;32m Vertices: ")
    for v in g.Lvertices:
        print(v.valor)
    print("\033[1;35m Arestas: ")
    for a in g.Larestas:
        print("orig: {0} dest: {1}".format(a.origem.valor, a.destino.valor)) #################

def caso_4(g): #busca em largura
    valor = input("\033[1;36mDigite o valor de origem e o valor de destino separado por vírgula Ex. o,d: \033[1;97m").split(',')
    if len(valor) == 2:
        vo = vertice(valor[0])
        vd = vertice(valor[1])
        distancia = g.buscaLargura(vo, vd)
        if distancia > 0:
            print("\033[1;36ma menor distância entre os vertices {0} para {1} é\033[1;33m {2}".format(vo.valor, vd.valor, distancia))
        else:
            print("\033[1;36mNão há caminho de {0} para {1}".format(vo.valor, vd.valor))
    else:
        print("\033[1;36mnúmero de argumentos inválidos!")
       
def caso_5(g): #busca profundidade
    g.iniciaBuscaProfundidade()

def printMenu():
    print("\033[1;33m1 - Adicionar vertice",
          "\n2 - Adicionar aresta", 
          "\n3 - Imprimir grafo",
          "\n4 - Busca em largura",
          "\n5 - Busca em profundidade",
          "\n6 - Sair \033[1;33m")

if __name__ == "__main__":
    entrada = -1
    g = grafo()
    mendict = {1: caso_1, 2: caso_2, 3: caso_3, 4: caso_4, 5: caso_5}
    while True:
        try:
            printMenu()
            entrada = int(input("Opção: \033[1;97m"))
            if entrada == 6:
                break
            else:
                mendict[entrada](g)
            input("\033[1;33m>>>>tc enter:")
        except ValueError:
            pass
        os.system("cls")