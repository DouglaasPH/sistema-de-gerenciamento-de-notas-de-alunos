def calcular_media(notas, disciplina=""):
    if disciplina == "":
        media = sum(notas) / 4
        return media
    else:
        media = sum(notas) / 4
        return [disciplina, media]


def procurar_matricula_e_calcular_media():
    
    while True:
        matricula = input("Matrícula do aluno: ")
        disciplina = input("Disciplina: ").lower()
        
        media = 0
        matricula_encontrado = False
        
        
        with open('dados/notas.txt', 'r') as f:
            
            for linha in f:
                linha_array = linha.split()
                    
                if matricula in linha_array and disciplina in linha_array:
                    matricula_encontrado = True
                    notas_string = linha_array[2:6]
                    notas_int = list(map(int, notas_string))
                    media = calcular_media(notas_int)
            
        if not matricula_encontrado:
            print("Matrícula ou Dsiciplina não encontrada. Por favor, verifique novamente.")
        else:
            if media >= 7:
                print(f"Aluno aprovado na disciplina de {disciplina}.")
            else:
                print(f"Aluno reprovado na disciplina de {disciplina}.")
            
            print(f"Média do aluno: {media}")
            break