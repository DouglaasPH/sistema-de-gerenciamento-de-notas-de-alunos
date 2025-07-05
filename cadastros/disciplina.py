def cadastro_de_disciplina():
    print("Cadastro de disciplina ")
    
    disciplina = input("Disciplina: ").lower()
        
    with open("dados/disciplinas.txt","a") as f:
        f.write(f"{disciplina}\n")
    
    print("Disciplina cadastrado com sucesso!")
    print("---------------------------------------")