#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
  def simpleArraySum(qtd_elem, ar):
    soma = 0
    for i in range(qtd_elem):
      soma = soma + ar[i]
    print(soma)

  qtd_elem = int(input())
  elem = input().split()
  # converte os valores string de elem para inteiro
  ar = [int(val) for val in elem]

  erro = False

  if qtd_elem > 0:
    for i in range(qtd_elem):
      if ar[i] > 1000:
        erro = True
        break
    if erro == False:
      simpleArraySum(qtd_elem, ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
