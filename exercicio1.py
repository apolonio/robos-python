
#!/usr/bin/python3
'''
ATIVIDADE: RETIRAR ESPAÇOS DAS LINHAS
'''
minhasMusicas = open('musicas.txt', 'r')
musicas = minhasMusicas.readlines()

for index in range(len(musicas)):
    musicas[index] = musicas[index].rstrip('\n')

minhasMusicas.close()
