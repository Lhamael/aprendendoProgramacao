class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def list_to_tree(lista):
  if not lista:
      return None

  def helper(index):
      if index >= len(lista) or lista[index] is None:
          return None

      node = TreeNode(lista[index])
      node.left = helper(2 * index + 1)
      node.right = helper(2 * index + 2)

      return node
  return helper(0)

## Minha Resoluçao
"""
def countPathsWithSum(arvore, alvo):
  caminhosPossiveis = []
  def percorreArvore(arvore, lista):
      lista = lista.copy()
      temp = 0
      if arvore:
          temp = arvore.val
          lista.append(temp)
          if arvore.left:
              percorreArvore(arvore.left, lista)
          if arvore.right:
              percorreArvore(arvore.right, lista)
          caminhosPossiveis.append(lista)
          return
      return

  percorreArvore(arvore, [])
  qtdCaminhos = 0
  dicionario = {}

  def percorreLista(lista, alvo, qtdCaminhos):

      if len(lista) != 0:
          soma = 0
          for i in len(lista):
              soma += lista[i]
              if soma == alvo:
                  if lista[:i] not in dicionario:
                      dicionario[lista[:i]]
                      qtdCaminhos += 1
                  break
          return percorreLista(lista[1:], alvo, qtdCaminhos)
      return qtdCaminhos

  listaCaminhos = []
  for caminho in caminhosPossiveis:
      qtdCaminhos = percorreLista(caminho, alvo, qtdCaminhos)

  return qtdCaminhos
"""
## Resolução do professor
def countPathsWithSum(root, targetSum):
  if not root:
      return 0

  pathSumFromMe = countPathsWithSumFromNode(root, targetSum, 0)
  pathSumFromLeft = countPathsWithSum(root.left, targetSum)
  pathSumFromRight = countPathsWithSum(root.right, targetSum)

  return pathSumFromMe + pathSumFromLeft + pathSumFromRight

def countPathsWithSumFromNode(node, targetSum, currentSum):
  if not node:
      return 0

  currentSum += node.val
  totalPaths = 0

  if targetSum - currentSum == 0:
      totalPaths += 1

  totalPaths += countPathsWithSumFromNode(node.left, targetSum, currentSum)
  totalPaths += countPathsWithSumFromNode(node.right, targetSum, currentSum)
  return totalPaths

# fim da resolução

alvo = int(input())
input_str = input()
nos = [int(x) if x.strip().lower() != "none" else None for x in input_str.split(",")]
root = list_to_tree(nos)
print(countPathsWithSum(root, alvo))