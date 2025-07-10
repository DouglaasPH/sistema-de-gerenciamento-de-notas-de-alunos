# 📚 Sistema de Gerenciamento de Notas de Alunos

## 🎯 Objetivo do Projeto

Este projeto tem como finalidade aplicar os principais conceitos estudados ao longo da disciplina de Programação, por meio do desenvolvimento de um sistema simples e funcional para gerenciamento de notas de alunos. O sistema permite o cadastro de estudantes e disciplinas, registro de notas, cálculo de médias, verificação de aprovação/reprovação e geração de relatórios. Os dados são persistidos por meio de manipulação de arquivos.

## 🛠️ Funcionalidades Implementadas

- **Cadastro de Alunos**
  Nome, matrícula e curso.

- **Cadastro de Disciplinas**
  Nome da disciplina e código associado.

- **Registro de Notas**
  Associação de notas aos alunos e respectivas disciplinas.

- **Cálculo de Média**
  Cálculo automático da média final de cada aluno por disciplina.

- **Verificação de Aprovação/Reprovação**
  Baseado na média mínima exigida (ex.: 7.0).

- **Relatórios de Desempenho**
  Consulta por matrícula: mostra disciplinas, médias e situação.

- **Persistência de Dados**
  Todos os dados são salvos em arquivos `.txt`, garantindo que as informações não sejam perdidas ao encerrar o programa.

- **Modularização com Funções**
  Cada operação do sistema foi separada em funções para promover clareza, reutilização e organização do código.

- **Uso de Estruturas de Controle**
  O sistema utiliza `if`, `else`, `while` e `for` para controlar o fluxo da aplicação.

- **Função Recursiva**
  Implementada uma função recursiva para exibição do desempenho do aluno, reforçando o conceito estudado.

---

## 💻 Como Executar o Programa

1. **Pré-requisitos:**

   - Interpretador Python 3 instalado no computador.

2. **Execução:**

   - Certifique-se de que todos os arquivos estão na **pasta raiz** do projeto.
   - Abra o terminal (Prompt de Comando, PowerShell ou terminal do VS Code).
   - Navegue até a pasta onde o projeto foi salvo.
   - Execute o programa com o seguinte comando:

     ```bash
     python main.py
     ```

3. **Interação:**

   - Utilize os números exibidos no menu principal para acessar as funcionalidades (cadastro de aluno, notas, consulta, etc.).
   - Os dados inseridos serão salvos automaticamente em arquivos `.txt` localizados na pasta do projeto.

---

Deseja que eu atualize o nome do arquivo em outras partes do README também (como na estrutura de pastas)?

---

## 🖥️ Exemplo da Interface Interativa

```text
Sistema de Gerenciamento de Notas de Alunos

1- CADASTRO ALUNO
2- CADASTRO DISCIPLNAS
3- CADASTRO NOTAS
4- CALCULAR MÉDIA E VERIFICAR APROVAÇÃO/REPROVAÇÃO
5- DESEMPENHO DO ALUNO
6- SAIR

: 1
---------- Cadastro de aluno ----------
Nome: douglas
Matricula: 120349
Curso: ads
Aluno cadastrado com sucesso.
---------------------------------------

: 2
---------- Cadastro de Disciplina ----------
Disciplina: quimica
Disciplina cadastrada com sucesso!
---------------------------------------

: 3
---------- Cadastro de Notas ----------
Disciplina: quimica
Matricula: 120349
Primeira Nota: 1
Segunda Nota: 7
Terceira Nota: 10
Quarta Nota: 9
Notas cadastradas com sucesso.
---------------------------------------

: 4
Matrícula do aluno: 120349
Disciplina: quimica
Aluno reprovado na disciplina de quimica.
Média do aluno: 6.75
---------------------------------------

: 5
Matrícula do aluno: 120349
Aluno reprovado na disciplina de quimica com média igual a 6.75
---------------------------------------

: 6
Obrigado, tenha um bom dia!
```

---

## 📁 Estrutura dos Arquivos

```
root_folder/
├── cadastros/
│   ├── aluno.py              # Funções para cadastro de alunos
│   ├── disciplina.py         # Funções para cadastro de disciplinas
│   └── nota.py               # Funções para cadastro de notas
│
├── calculo_e_verificacao/
│   ├── media.py              # Funções para cálculo de médias
│   └── verificacao.py        # Funções para verificar aprovação/reprovação
│
├── dados/
│   ├── alunos.txt            # Armazena os dados dos alunos cadastrados
│   ├── disciplinas.txt       # Armazena os dados das disciplinas
│   └── notas.txt             # Armazena as notas lançadas
│
├── relatorio/
│   └── relatorio.py          # Geração de relatórios de desempenho
│
├── main.py                   # Arquivo principal para execução do sistema
└── README.md                 # Documento explicativo do projeto
```
