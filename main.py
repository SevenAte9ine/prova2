from Livro import Livro
l1 = Livro(None, None, None)
while True:
  esc = input("""Escolha se deseja inserir ou remover um livro da fila. Insira 1 para inserir, e 2 para remover: """)
  if esc == '1':
    l1.adicionar(input("Insira um titulo: "), input("Insira um autor: "), input("Insira um nome: "), input("Insira um ID: "))
  if esc == '2':
    l1.remover()
