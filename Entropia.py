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
