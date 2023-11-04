import csv
import os

nome_arquivo = input('Digite o nome do arquivo: ')
if os.path.exists(f'{nome_arquivo}.csv'):
    arquivo = open(f'{nome_arquivo}.csv','a')
else:
    arquivo = open(f'{nome_arquivo}.csv','w')
    arquivo.write('Nome;NP1;NP2;Media;Exame;Media Final;Resultado\n')


alunos = (input('Quantidade de alunos: '))


#ALUNOS
while alunos.isnumeric() == False:
    print('Digite um número!')
    alunos = (input('Quantidade de alunos: '))
if alunos.isnumeric():
    alunos = int(alunos)

for i in range(1, alunos + 1):

#NOME
    print(f'Aluno {i}')
    nome = input('Nome: ')
    arquivo.write(f'\n{nome};')

    while nome.isalpha() == False:
        print('Digite um nome!')
        nome = input('Nome: ')

    if nome.isalpha():
#NP1
        np1 = (input('NP1: '))
        arquivo.write(f'{np1};')
        while np1.isnumeric() == False:
            print('Digite um número válido!')
            np1 = (input('NP1: '))
        if np1.isnumeric():
            np1 = float(np1)
            while np1 > 10 or np1<0:
                print('O valor da NP1 não pode ser maior do que 10!')
                np1 = (input('NP1: '))
                np1 = float(np1)


#NP2
            np2 = (input('NP2: '))
            arquivo.write(f'{np2};')
            while np2.isnumeric() == False:
                print('Digite um número válido!')
                np2 = (input('NP2: '))
            if np2.isnumeric():
                np2 = float(np2)
                while np2 > 10:
                    print('O valor da NP2 não pode ser maior do que 10!')
                    np2 = (input('NP2: '))
                    np2 = float(np2)


#MEDIA
                media = (np1 + np2) / 2
                print(f'MEDIA = {media:.2f}')
                arquivo.write(f'{media};')
                if media >= 7:
                    print('Aluno Aprovado\n')
                    mf = media
                    arquivo.write(f'---;')
                    arquivo.write(f'---;')
                    arquivo.write('Aprovado')


                else:
#EXAME
                    ex = (input('Nota do exame: '))
                    while ex.isnumeric() == False:
                        print('Digite um número válido!')
                        ex = (input('Nota do exame: '))
                    if ex.isnumeric():
                        ex = float(ex)
                        arquivo.write(f'{ex};')
                        while ex > 10:
                            print('O valor do exame não pode ser maior do que 10!')
                            ex = (input('Nota do exame: '))
                            ex = float(ex)

#MEDIAFINAL
                        mf = (media + ex) / 2
                        arquivo.write(f'{mf};')
                        if mf >= 5:
                            print(f'Media final: {mf:.2f}')
                            print('Aluno Aprovado\n')
                            arquivo.write('Aprovado')
                        else:
                            print(f'Media final: {mf:.2f}')
                            print('Aluno Reprovado\n')
                            arquivo.write('Reprovado')

#CASO NÃO FOR NOME
    else:
        print('Digite um nome!')
        nome = input('Nome: ')

arquivo.close

