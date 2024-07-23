# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os
import json


def listar(lista):
    print('\nLista de Tarefas:\n')
    if lista == []:
        print('Nenhum tarefa existente!\n')
    else:
        for i, t in enumerate(lista):
            print(f'{i+1} - {t}')
            print()


def refazer(lista_tarefas, backup):
    if backup == []:
        print('\nNenhum tarefa para refazer!\n')
    else:
        tarefa = backup.pop()
        print(f'\nA tarefa "{tarefa}" foi adicionada!')
        lista_tarefas.append(tarefa)
    listar(lista_tarefas)


def desfazer(lista_tarefas, backup):
    if lista_tarefas == []:
        print('\nNenhum tarefa para desfazer!\n')
    else:
        tarefa = lista_tarefas.pop()
        print(f'\nA tarefa "{tarefa}" foi removida!')
        backup.append(tarefa)
    listar(lista_tarefas)


backup = []
try:
    with open('./intermediario/aula116.json', 'r', encoding='utf8') as arquivo:
        lista_tarefas = json.load(arquivo)
except Exception:
    print('Erro ao abrir arquivo!')
    lista_tarefas = []

comandos = {
    'listar': lambda: listar(lista_tarefas),
    'desfazer': lambda: desfazer(lista_tarefas, backup),
    'refazer': lambda: refazer(lista_tarefas, backup),
    'clear': lambda: os.system('cls'),
}

while True:
    try:
        print('Comandos: listar, desfazer, refazer e sair')
        tarefa = input('Digite uma tarefa ou comando:')
        if tarefa.lower() == 'sair':
            break
        if comandos.get(tarefa) is not None:
            comando = comandos.get(tarefa)
            comando()
        else:
            lista_tarefas.append(tarefa)
    except Exception as e:
        print(e)

with open('./intermediario/aula116.json', 'w', encoding='utf8') as arquivo:
    if arquivo:
        json.dump(lista_tarefas, arquivo, ensure_ascii=False, indent=2)
        print('\nArquivo salvo com sucesso!\n')
