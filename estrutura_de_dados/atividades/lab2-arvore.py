# essa é uma função da classe raiz.
alturaArvore = {}
alturaArvore[0] = 0
def mostra_arvore_e_altura(raiz):
  arvore("", raiz)
  print()
  print("altura: ", altura(raiz) ,sep="")


def arvore(prefixo, raiz):
  print(prefixo, raiz.dado,sep="")
  if raiz.dir:
    arvore(prefixo+"__", raiz.dir)
  if raiz.esq:
    arvore(prefixo+"__", raiz.esq)

def altura(raiz):
  if raiz is None or not (raiz.esq or raiz.dir):
      return 0

  return 1 + max(altura(raiz.esq), altura(raiz.dir))
