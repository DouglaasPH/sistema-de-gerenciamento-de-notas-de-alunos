import sys
import os

# Adicionando a raiz do projeto ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculo_e_verificacao.media import calcular_media



def relatorio():
    resultado_final = []
    
    while True:
        matricula = input("Matrícula do aluno: ")
        
        with open('dados/notas.txt', 'r') as f:
            
            for linha in f:
                linha_array = linha.split()
                
                if matricula in linha_array:
                    notas_string = linha_array[2:6]
                    notas_int = list(map(int, notas_string))
                    resultado = calcular_media(notas_int, linha_array[0])
                    
                    if resultado[1] > 7:
                        resultado.append(True)
                    else:
                        resultado.append(False)

                    resultado_final.append(resultado)
                    
        if len(resultado_final) == 0:
            print("O aluno não possui notas ou não foi possível encontrar o aluno.")
        else:
            break
    
    
    for values in resultado_final:
        if values[1] >= 7:
            print(f"Aluno aprovado na disciplina de {values[0]} com média igual a {values[1]}")
        else:
            print(f"Aluno reprovado na disciplina de {values[0]} com média igual a {values[1]}")
    print("---------------------------------------")