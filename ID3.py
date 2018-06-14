import math
import scipy.stats as st
#import pandas as pd

#Calculo de entropia, recebe um array com a quantidade de ocorrencias de cada classe
def entropia(dist_geral):
    #Zera o total
    total = 0

    #Para cada distribuiçao de um valor de classe
    for dist_classe in dist_geral:

       #prop recebe a razao entre a distribuiçao daquele valor de classe pelo total de ocorrencias
       prop = dist_classe / sum(dist_geral)
       if prop != 0:
           total += prop * math.log(prop, 2)
       else:
           total += 0
       total *= -1
    return total

#Calculo de ganho de informação. Recebe o array de ocorrencias de cada classe e a distribuição de classes para cada valor do atributo EX: ([6,6],[ [4,2],[2,4] ])
def ganho_info(dist_geral,dist_atrib):

    #Inicio o total com a entropia do conjunto pai
    total = entropia(dist_geral)

    #Para cada array de distribuiçao de classes dado o valor do atributo
    for valor in dist_atrib:

        #Prop recebe a proporçao de instancias com aquele valor pelo total
        prop = sum(valor) / sum(dist_geral)
        #Calculo a entropia do sub conjunto
        entropia_sub = entropia(valor)
        #Subtraio da entropia do conjunto pai
        total -= prop * entropia_sub
    return total

class No:
    def __init__(self, atributo=None, exemplos=None):
        self.atributo = atributo
        self.exemplos = exemplos
        self.prox = None

    def inicia_prox(self):
        for valor in exemplos[atributo]:
            prox[valor] = None

class No_Folha:
    def __init__(self, classe=None):
        self.classe = classe

#Recebe um conjunto de exemplos e uma lista de atributos e devolve qual o atributo que proporciona o maior ganho de informação
def melhor_atributo(exemplos, atributos, atr_alvo):
    melhor = None
    #obter lista de distribuicao geral
    pos = exemplos[atr_alvo].count("+")
    neg = exemplos[atr_alvo].count("-")
    dist_geral = [pos,neg]
    ganho_atr_maior = 0
    #para cada atributo
    for atributo in atributos:
        #obter lista de distribuicao daquele atributo
        dist_atr = None
        for valor in atributo:
            #obter distribuiçoes por valor para criar a lista de distribuiçoes do atributo
            for exemplo in exemplos:
                if exemplo[atributo] == valor:
                    if exemplo[atr_alvo] == "+": pos_atr++
                    if exemplo[atr_alvo] == "-": neg_atr++
            #adiciono a distribuição daquele valor para a lista de distribuiçoes do atributo
            dist_atr.append([pos_atr,neg_atr])
            pos_atr = 0
            neg_atr = 0
        #checo o ganho de informaçao do atributo testado e se for melhor, atualizo
        ganho_atr = ganho_info(dist_geral, dist_atr)
        if ganho_atr > ganho_atr_maior:
            melhor = atributo
            ganho_atr_maior = ganho_atr
        #obter o ganho de informaçao daquele atributo
        #se for maior que o maior, altero a variavel melhor
    return melhor
    


def ID3 (exemplos, atr_alvo, atributos):
    #Criar nó raiz
    raiz = No()

    #Caso de parada onde todos os exemplos são positivos
    if ((exemplos[atr_alvo].count("-") == 0)):
        raiz = No_Folha("+")
        return raiz

    #Caso de parada onde todos os exemplos são negativos
    if ((exemplos[atr_alvo].count("+") == 0)):
        raiz = No_Folha("-")
        return raiz
    #Caso de parada de não haver mais atributos -> retorna classe mais frequente em exemplos
    if len(atributos) == 0:
        if (exemplos[atr_alvo].count("+")) >= (exemplos[atr_alvo].count("-")):
            raiz = No_Folha("+")
        else:
            raiz = No_Folha("-")
        return raiz
    #Begin

    #Selecionar atributo que proporciona maior ganho de informação
    atr_raiz = melhor_atributo(exemplos, atributos, atr_alvo)
    #Atribuir esse valor ao atributo do nó raiz
    raiz.atributo = atr_raiz
    #Para cada valor desse atributo
    for valor in atr_raiz:
          #Adicionar ramo para o teste A = v
          #Exemplos_v é o subconjunto onde A = v
          for exemplo in exemplos:
              if exemplo[atr_raiz] == valor:
                  exemplos_v.update(exemplo)
          #Se exemplos_v for vazio, criar nó folha com valor de classe mais comum em exemplos
          if !(exemplos_v):
              classe_dom = classe_dominante(exemplos)
              n = No_Folha(classe_dom)
              raiz.prox[valor] = n
          #Se não for vazio, executar ID3(Exemplos_v, atr_alvo, atributos - {A})
          else:
              atributos_v = atributos
              del atributos_v[atr_raiz]
              raiz.prox[valor] = ID3(exemplos_v, atr_alvo, atributos_v)
  #End Loop

  #Return nó raiz
  return raiz

play_tennis= [{'aparencia':'ensolarado','temperatura':'quente','umidade':'alta','vento':'fraco','jogar_tenis':'-'}
              {'aparencia':'ensolarado','temperatura':'quente','umidade':'alta','vento':'forte','jogar_tenis':'-'}
              {'aparencia':'nublado','temperatura':'quente','umidade':'alta','vento':'fraco','jogar_tenis':'+'}
              {'aparencia':'chuva','temperatura':'moderada','umidade':'alta','vento':'fraco','jogar_tenis':'+'}
              {'aparencia':'chuva','temperatura':'fria','umidade':'normal','vento':'fraco','jogar_tenis':'+'}
              {'aparencia':'chuva','temperatura':'fria','umidade':'normal','vento':'forte','jogar_tenis':'-'}
              {'aparencia':'nublado','temperatura':'fria','umidade':'normal','vento':'forte','jogar_tenis':'+'}
              {'aparencia':'ensolarado','temperatura':'moderada','umidade':'alta','vento':'fraco','jogar_tenis':'-'}
              {'aparencia':'ensolarado','temperatura':'fria','umidade':'normal','vento':'fraco','jogar_tenis':'+'}
              {'aparencia':'chuva','temperatura':'moderada','umidade':'normal','vento':'fraco','jogar_tenis':'+'}
              {'aparencia':'ensolarado','temperatura':'moderada','umidade':'normal','vento':'forte','jogar_tenis':'+'}
              {'aparencia':'nublado','temperatura':'moderada','umidade':'alta','vento':'forte','jogar_tenis':'+'}
              {'aparencia':'nublado','temperatura':'quente','umidade':'normal','vento':'fraco','jogar_tenis':'+'}
              {'aparencia':'chuva','temperatura':'moderada','umidade':'alta','vento':'forte','jogar_tenis':'-'}]

atributos_play_tenis= {'aparencia':['ensolarado','nublado','chuva'],
                       'temperatura':['quente','moderada','fria'],
                       'umidade':['alta','normal'],
                       'vento':['forte','fraco']}
                                                                              
ID3(play_tennis, atributos_play_tenis, 'jogar_tenis')
