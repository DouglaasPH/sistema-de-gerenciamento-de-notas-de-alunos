from cadastros.aluno import *
from cadastros.disciplina import *
from cadastros.nota import *
from calculo_e_verificacao.media import *
from relatorio.relatorio import *
from time import sleep
import os
os.system('cls')


def main():
    
    while True:
        print("Sistema de Gerenciamento de Notas de Alunos\n")
        print("1- CADASTRO ALUNO")
        print("2- CADASTRO DISCIPLNAS")
        print("3- CADASTRO NOTAS")
        print("4- CALCULAR MÉDIA E VERIFICAR APROVAÇÃO/REPROVAÇÃO")
        print("5- DESEMPENHO DO ALUNO")
        print("6- SAIR")
        entrada = input("\n: ")
        
        match entrada:
            case "1":
                cadastro_de_aluno()
            case "2":
                cadastro_de_disciplina()               
            case "3":
                cadastro_de_notas()               
            case "4":
                procurar_matricula_e_calcular_media()               
            case "5":
                relatorio()
            case "6":
                print("Obrigado, tenha um bom dia!")
                break
            case _:
                print("Você digitou um valor inválido. Tente novamente.")
                print("---------------------------------------")
        sleep(1)
        print("\n")
        
main()