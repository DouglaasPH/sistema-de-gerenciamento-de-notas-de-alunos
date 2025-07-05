def cadastro_de_aluno():
    print("---------- Cadastro de aluno ----------")
    
    nome = input("Nome: ").lower()
    matricula = input("Matricula: ")
    curso = input("Curso: ").lower()
    
    aluno = f"{nome} {matricula} {curso}\n"
    
    with open("dados/alunos.txt","a") as f:
        f.write(aluno)
    
    print("Aluno cadastrado com sucesso.")
    print("---------------------------------------")