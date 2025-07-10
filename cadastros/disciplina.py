def cadastro_de_disciplina():
    print("---------- Cadastro de Disciplina ----------")
    
    disciplina = input("Disciplina: ").lower()
        
    with open("dados/disciplinas.txt","a") as f:
        f.write(f"{disciplina}\n")
    
    print("Disciplina cadastrada com sucesso!")
    print("---------------------------------------")