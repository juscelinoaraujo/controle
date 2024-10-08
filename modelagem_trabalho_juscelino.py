# -*- coding: utf-8 -*-
"""Modelagem_Trabalho_Juscelino.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11_MKOocBNV-1fc_ZbvSxM-sR7FnJkVcD
"""

# importação de biblioteca usada para geração de matriz
import numpy as np

def calcula_elemento(a, b, c, d):
  """Calcula um elemento da tabela de Routh.

  Args:
    a: Coeficiente a.
    b: Coeficiente b.
    c: Coeficiente c.
    d: Coeficiente d.

  Returns:
    O valor calculado do elemento.
  """
  if a != 0:
    return (a*b - c*d)/a
  else:
    return 0

def gera_tabela(vetor):
  """Gera a tabela de Routh a partir do vetor dos coeficientes do polinômio.

  Args:
    vetor: Vetor de coeficientes.

  Returns:
    A tabela de Routh gerada.
  """
  n_col = len(vetor)//2 + len(vetor)%2
  n_lin = 2*n_col
  tabela = np.zeros((n_lin, n_col))
  for i in range(n_col):
    tabela[0, i] = vetor[2*i]
    if (2*i+1) < len(vetor):
      tabela[1, i] = vetor[2*i+1]
  for j in range(2, n_lin):
    k = n_col - j//2
    for i in range(k):
      a = tabela[j-1, 0]
      b = tabela[j-2, i+1]
      c = tabela[j-2, 0]
      d = tabela[j-1, i+1]
      tabela[j, i] = calcula_elemento(a, b, c, d)
  return tabela

def muda_sinal(novo, antigo):
  """ Verifica se há mudança de sinal.

  Args:
    novo: Novo valor.
    antigo: Valor antigo.

  Returns:
    True se houver mudança de sinal, False caso contrário.
  """
  if novo*antigo < 0:
    return True
  else:
    return False

def num_mudancas_sinal(col):
  """ Conta o número de mudanças de sinal.

  Args:
    col: Coluna da tabela de Routh.

  Returns:
    O número de mudanças de sinal.
  """
  return sum([muda_sinal(novo, antigo) for novo, antigo in zip(col[1:], col[:-1])])

def num_polos_inst(vetor):
  """ Conta o número de polos instáveis.

  Args:
    vetor: Vetor de coeficientes.

  Returns:
    O número de polos instáveis.
  """
  return num_mudancas_sinal(gera_tabela(vetor)[:,0])

print(num_polos_inst([1, 3, 6, 12, 8]))