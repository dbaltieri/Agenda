

from sys import *
button = True

def createFile():
	file = open('Agenda.txt', 'w')
	file.write('\t\tAgenda 2018 \n\nNOME\t\tTELEFONE\n')
	print('Agenda criada com sucesso ! ')
	file.close()

def inserirContato():
	nome = input('Entre com o nome do contato: ')
	telefone = input('Entre com o numero desse contato: ')
	file = open('Agenda.txt', 'a')
	file.write('%s\t%s'%(nome, telefone)+'\n')
	file.close()


def buscarByname(busca):
	contato = {}
	file = open('Agenda.txt')
	data = file.read()
	file.close()
	data = data.split('\n')
	#print(data)
	for i in data:
		if len(i) > 3:
			if i[0]=='\t': continue
			if i[0]=='N': continue
			i = i.split('\t')
			contato[i[0]] = {i[0]:i[1]}
			#print(contato[i[0]])
	for n in contato.keys():
		#print('This is n', n)
		if n == busca:
			print('Encontrado',contato[n])
			return
		else:
			continue
	print('O nome nao foi encontrado na agenda ')

def editarContato():
	print('This function isnt built yet')

def apagarContato():
	print('This function isnt built yet')

#createFile()
#inserirContato()

def mostraTabela():
	print(' --------------------------------------------------------')
	print('|\tOptions\t\tComands\t\t\t\t|')
	print(' --------------------------------------------------------')
	print('|\t%s\t\t%s\t\t|' %('C','Criar nova agenda '))
	print('|\t%s\t\t%s\t\t|' %('N','Criar novo contato '))
	print('|\t%s\t\t%s\t|' %('B','Buscar contato por nome '))
	print('|\t%s\t\t%s\t\t\t|' %('E','Editar contato '))
	print('|\t%s\t\t%s\t\t\t|' %('A','Apagar contato '))
	print(' --------------------------------------------------------')



def mainMenu(Option):

	if Option == 'S':
		print('Finalizando agenda ....')
		button = False
		exit(0)
	elif Option == 'C':
		createFile()
	elif Option == 'N':
		inserirContato()
	elif Option == 'B':
		buscarByname(input('Entre com o nome que deseja buscar: '))
	elif Option == 'E':
		editarContato()
	elif Option == 'A':
		apagarContato()
	else:
		print('Comando invalido, entre com algum comado valido ! ')

while button == True:
	mostraTabela()
	mainMenu(input('Digite a opcao desejada: '))

