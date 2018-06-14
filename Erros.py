import math
import scipy.stats as st

class Erros:
 #Metodo de inicialização da classe de erro
 def __init__(self, error_avg, n_testes, confianca):
   self.error_avg = error_avg
   self.n_testes = n_testes
   self.confianca = 1 - (1 - confianca)/2
   #Calculo do erro padrao
   self.std_error = math.sqrt((self.error_avg * (1 - self.error_avg)) / self.n_testes)

 #Metodo para calculo do erro verdadeiro
 #Retorna uma tupla com o erro verdadeiro mínimo e máximo

 def erro_verdadeiro(self):
   erro_min = self.error_avg - (st.norm().ppf(self.confianca) * self.std_error)
   erro_max = self.error_avg + (st.norm().ppf(self.confianca) * self.std_error)
   return erro_min, erro_max
