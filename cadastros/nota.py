def verificar_disciplina(disciplina):
    with open("dados/disciplinas.txt", "r") as f:
        arquivo = f.read().split()
        
        if disciplina in arquivo:
            return True
        else:
            return False


def verificar_matricula(matricula):
    with open("dados/alunos.txt", "r") as f:
        arquivo = f.read().split()
        
        if matricula in arquivo:
            return True
        else:
            return False


def cadastro_de_notas():
    print("---------- Cadastro de Notas ----------")
    
    
    while True:
        disciplina = input("Disciplina: ").lower()
        is_disciplina = verificar_disciplina(disciplina)
        
        if not is_disciplina:
            print("A disciplina não existe. Por favor, digite novamente.")
        else:
            matricula = input("Matricula: ")
            is_matricula = verificar_matricula(matricula)
            
            if is_matricula:
                nota1 = input("Primeira Nota: ")
                nota2 = input("Segunda Nota: ")
                nota3 = input("Terceira Nota: ")
                nota4 = input("Quarta Nota: ")
                
                with open("dados/notas.txt","a") as f:
                    f.write(f"{disciplina} {matricula} {nota1} {nota2} {nota3} {nota4}\n")
                    break
            else:
                print("A matrícula não existe. Por favor, digite novamente.")
    
    print("Notas cadastradas com sucesso.")
    print("---------------------------------------")