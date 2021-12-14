from Autor import Autor

class Livro(Autor):

	def __init__(self, id, titulo, autor):
	    self.id = id
	    self.titulo = titulo
	    self.inicioId = None
	    self.inicioTi = None
	    self.inicio = None
	    self.fimId = None
	    self.fimTi = None
	    self.fim = None
	    self.tamanho = 0

	def adicionar(self, titulo, autor, nome, id):
		autor = Autor( nome, id )
		if self.tamanho == 0:
			self.inicioId = autor
			self.inicioTi = autor
			self.inicio = autor
			self.fimId = autor
			self.fimTi = autor
			self.fim = autor
		else:
			self.fim.proximoId = autor
			self.fim.proximoNome = autor
			self.fim = autor
		self.tamanho += 1
		print("Quatidade de livros inseridos: ",self.tamanho)

	def remover(self):
		if self.tamanho == 0:
			print( "Fila Vazia!")
		elif self.tamanho == 1:
			self.inicio = None
			self.inicioId = None
			self.inicioTi = None
			self.fimId = None
			self.fimTi = None
			self.fim = None
			self.tamanho = 0
		else:
			self.inicioId = self.inicio.proximoId
			self.inicioTi = self.inicio.proximoNome
			self.inicio = self.inicio.proximo
			self.tamanho -= 1
			print("Tamanho após a remoção: ", self.tamanho)
